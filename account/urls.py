from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    EmailTokenObtainPairView,
    RegisterAPIView,
    RoleAPIView,
    RoleDetailAPIView,
    PermissionAPIView,
    PermissionDetailAPIView,
    MethodAPIView,
    MethodDetailAPIView,
)

urlpatterns = [
    re_path(r"^register/$", RegisterAPIView.as_view()),
    path("token/obtain/", EmailTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("role/", RoleAPIView.as_view()),
    path("role/<id>/", RoleDetailAPIView.as_view()),
    path("permission/", PermissionAPIView.as_view()),
    path("permission/<id>/", PermissionDetailAPIView.as_view()),
    path("method/", MethodAPIView.as_view()),
    path("method/<id>/", MethodDetailAPIView.as_view()),
]
