from django.urls import path

from apps.access.views import LoginAPIView, SignUpAPIView
from apps.common.router import router

urlpatterns = [
    path("sign-up/", SignUpAPIView.as_view(), name="sign-up"),
    path("login/", LoginAPIView.as_view(), name="login"),
] + router.urls
