from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import EmailTokenObtainPairView, RegisterView

urlpatterns = [
    re_path(r"^register/$", RegisterView.as_view(), name="register"),
    path(
        "token/obtain/",
        EmailTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
