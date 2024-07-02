from apps.blog.views import BlogCUDAPIViewSet, BlogListAPIViewSet
from apps.common.router import router

app_name = "blog"

API_URL_PREFIX = "api/blog/"

router.register(f"{API_URL_PREFIX}cud", BlogCUDAPIViewSet)
router.register(f"{API_URL_PREFIX}list", BlogListAPIViewSet)

urlpatterns = [] + router.urls
