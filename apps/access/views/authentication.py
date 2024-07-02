from rest_framework import status
from rest_framework.authtoken.models import Token

from apps.access.serializers import LoginResponseSerializer, LoginSerializer, SignUpSerializer
from apps.common.views import AppAPIView, NonAuthenticatedAPIMixin


class SignUpAPIView(NonAuthenticatedAPIMixin, AppAPIView):
    """Used to create user in the application if they not exist."""

    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.get_valid_serializer()
        serializer.save()
        return self.send_response(status_code=status.HTTP_201_CREATED, data="User signed up successfully.")


class LoginAPIView(NonAuthenticatedAPIMixin, AppAPIView):
    """Used to login user into the application."""

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_valid_serializer()
        user = serializer.validated_data["user"]
        return self.send_response(
            data=LoginResponseSerializer(user).data,
        )


class RefreshAuthTokenAPIView(AppAPIView):
    """Refresh APIView for the services to authenticate tokens."""

    def get(self, *args, **kwargs):
        user = self.get_user()
        if user:
            return self.send_response(
                data=LoginResponseSerializer(user).data,
            )


class LogoutAPIView(AppAPIView):
    """Invalidate a token and logout user."""

    def post(self, *args, **kwargs):
        user = self.get_authenticated_user()
        if user:
            Token.objects.filter(user=user).delete()
            return self.send_response("User logged out.")
        return self.send_error_response()
