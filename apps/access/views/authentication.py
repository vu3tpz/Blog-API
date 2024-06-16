from rest_framework import status
from rest_framework.authtoken.models import Token

from apps.access.models import User
from apps.access.serializers import LoginSerializer, SignUpSerializer
from apps.common.views import AppAPIView, NonAuthenticatedAPIMixin


def logged_in_response(user, token):
    return {
        "user": {
            "id": user.id,
            "uuid": str(user.uuid),
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "user_type": user.type,
        },
        "token": token.key,
    }


class SignUpAPIView(NonAuthenticatedAPIMixin, AppAPIView):
    """Used to create user in the application if they not exist."""

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.send_response(status_code=status.HTTP_201_CREATED)
        return self.send_error_response(serializer.errors)


class LoginAPIView(NonAuthenticatedAPIMixin, AppAPIView):
    """Used to login user into the application."""

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, _ = Token.objects.get_or_create(user=user)
            return self.send_response(
                data=logged_in_response(user, token),
            )
        return self.send_error_response("User not found")
