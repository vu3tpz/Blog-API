from django.urls import path

from apps.access.views import LoginAPIView, LogoutAPIView, RefreshAuthTokenAPIView, SignUpAPIView

app_name = "access"

API_URL_PREFIX = "api/access/"

urlpatterns = [
    path(f"{API_URL_PREFIX}sign-up/", SignUpAPIView.as_view(), name="sign-up"),
    path(f"{API_URL_PREFIX}login/", LoginAPIView.as_view(), name="login"),
    path(f"{API_URL_PREFIX}refresh-token/", RefreshAuthTokenAPIView.as_view(), name="refresh-token"),
    path(f"{API_URL_PREFIX}logout/", LogoutAPIView.as_view(), name="logout"),
]
