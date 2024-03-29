from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from common.view import CommonCreateListAPIView, CommonDetailAPIView
from .serializers import (
    TokenObtainPairSerializer,
    UserSerializer,
    RoleSerializer,
    PermissionSerializer,
    MethodSerializer,
)
from .models import Role, Permission, Method
from common.permissions import CustomRolePermission


# Create your views here.
class RegisterAPIView(APIView):
    """
    APIView user to Register
    """

    def post(self, *args, **kwargs):
        serializer = UserSerializer(data=self.request.data)
        if serializer.is_valid():
            get_user_model().objects.create_user(**serializer.validated_data)
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(data={"errors": serializer.errors}, status=HTTP_400_BAD_REQUEST)


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class RoleAPIView(CommonCreateListAPIView):
    """
    APIView used to `create` and `list` Role
    """

    permission_classes = [CustomRolePermission]
    serializer_class = RoleSerializer
    model_class = Role


class RoleDetailAPIView(CommonDetailAPIView):
    """
    APIView used to get the `detail` view, `Update` and `Delete` of particular data
    """

    serializer_class = RoleSerializer
    model_class = Role


class PermissionAPIView(CommonCreateListAPIView):
    """
    APIView used to `create` and `list` Permission
    """

    serializer_class = PermissionSerializer
    model_class = Permission


class PermissionDetailAPIView(CommonDetailAPIView):
    """
    APIView used to get the `detail` view, `Update` and `Delete` of particular data
    """

    serializer_class = PermissionSerializer
    model_class = Permission


class MethodAPIView(CommonCreateListAPIView):
    """
    APIView used to `create` and `list` Method
    """

    serializer_class = MethodSerializer
    model_class = Method


class MethodDetailAPIView(CommonDetailAPIView):
    """
    APIView used to get the `detail` view, `Update` and `Delete` of particular data
    """

    serializer_class = MethodSerializer
    model_class = Method
