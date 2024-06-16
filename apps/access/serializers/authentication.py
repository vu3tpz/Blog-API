from rest_framework import serializers

from apps.access.models import User
from apps.common.serializers import AppWriteOnlyModelSerializer


class SignUpSerializer(AppWriteOnlyModelSerializer):
    """Serializer to create User"""

    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta(AppWriteOnlyModelSerializer.Meta):
        model = User
        fields = ["first_name", "last_name", "username", "email", "password", "confirm_password"]

    def validate_password(self, password):
        """Validate the password."""

        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")

        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError("Password must contain at least one digit.")

        if not any(char.isupper() for char in password):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")

        if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" for char in password):
            raise serializers.ValidationError("Password must contain at least one special character.")

        return password

    def validate_username(self, username):
        """Validate the username."""

        if len(username) < 6:
            raise serializers.ValidationError("Username must be at least 6 characters long.")

        return username

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        # Validate the password are matches against confirm_password
        if password != confirm_password:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            username=validated_data["username"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )
        return user
