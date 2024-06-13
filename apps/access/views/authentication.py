from apps.access.models import User
from apps.access.serializers import SignUpSerializer
from apps.common.views import AppModelCreateAPIViewSet, NonAuthenticatedAPIMixin


class SignUpAPIViewSet(NonAuthenticatedAPIMixin, AppModelCreateAPIViewSet):
    """Used to create user in the application if they not exist."""

    serializer_class = SignUpSerializer
    queryset = User.objects.all()
