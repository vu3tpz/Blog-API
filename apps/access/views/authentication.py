from rest_framework import status

from apps.access.serializers import SignUpSerializer
from apps.common.views import AppAPIView, NonAuthenticatedAPIMixin


class SignUpAPIViewSet(NonAuthenticatedAPIMixin, AppAPIView):
    """Used to create user in the application if they not exist."""

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.send_response(status=status.HTTP_201_CREATED)
        return self.send_error_response(serializer.errors)
