from apps.blog.views import BlogCUDAPIViewSet
from apps.common.router import router

app_name = "blog"

API_URL_PREFIX = "api/blog/"

router.register(f"{API_URL_PREFIX}cud", BlogCUDAPIViewSet)

urlpatterns = [] + router.urls
