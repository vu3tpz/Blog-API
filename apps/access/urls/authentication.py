from django.urls import path

from apps.access.views import SignUpAPIViewSet
from apps.common.router import router

urlpatterns = [
    path("sign-up/", SignUpAPIViewSet.as_view()),
] + router.urls
