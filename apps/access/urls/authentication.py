from django.urls import path

from apps.access.views import LoginAPIView, LogoutAPIView, RefreshAuthTokenAPIView, SignUpAPIView

urlpatterns = [
    path("sign-up/", SignUpAPIView.as_view(), name="sign-up"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("refresh-token/", RefreshAuthTokenAPIView.as_view(), name="refresh-token"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
]
