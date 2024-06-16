from rest_framework import serializers

from apps.access.models import User
from apps.common.serializers import AppWriteOnlyModelSerializer


class SignUpSerializer(AppWriteOnlyModelSerializer):
    """Serializer to create User"""

    password = serializers.CharField(write_only=True)

    class Meta(AppWriteOnlyModelSerializer.Meta):
        model = User
        fields = ["first_name", "last_name", "email", "password", "username"]

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            username=validated_data["username"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )
        return user
