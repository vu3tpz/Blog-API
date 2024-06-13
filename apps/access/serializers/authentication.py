from apps.access.models import User
from apps.common.serializers import AppWriteOnlyModelSerializer


class SignUpSerializer(AppWriteOnlyModelSerializer):
    """Serializer to create User"""

    class Meta(AppWriteOnlyModelSerializer.Meta):
        model = User
        fields = ["first_name", "last_name", "email", "password"]
