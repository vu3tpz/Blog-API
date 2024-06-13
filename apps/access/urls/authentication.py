from apps.access.views import SignUpAPIViewSet
from apps.common.router import router

router.register("sign-up", SignUpAPIViewSet)

urlpatterns = [] + router.urls
