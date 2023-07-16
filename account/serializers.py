from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Method, Permission, Role, User


class TokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD


class MethodSerializer(serializers.ModelSerializer):
    """
    Serializer for `Method` model
    """

    class Meta:
        model = Method
        fields = ("id", "name")


class PermissionSerializer(serializers.ModelSerializer):
    """
    Serializer for `Permission` model
    """

    class Meta:
        model = Permission
        fields = ("id", "name", "description", "method")


class RoleSerializer(serializers.ModelSerializer):
    """
    Serializer for `Role` model,

    Here `permission` is `ManyToMany` field so that we need to use `permission = PermissionSerializer(many=True)`,
    But the problem is we can use that method for `GET` but for `POST` we can't use so we use the below method to
    handle both operation in same Serilaizer.
    """

    permission = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    class Meta:
        model = Role
        fields = ("id", "name", "description", "permission")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["permission"] = PermissionSerializer(
            instance.permission.all(), many=True
        ).data
        return representation


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for `User` model
    """

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "password", "role", "joined_on")
