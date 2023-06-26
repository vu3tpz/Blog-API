from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User, Role, Permission, Method, RolePermission
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', 'description')

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name', 'description')

class MethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Method
        fields = ('id', 'name')

class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = ('id', 'role', 'permission', 'method')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'role', 'joined_on')