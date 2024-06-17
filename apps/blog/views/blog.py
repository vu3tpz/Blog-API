from apps.blog.models import Blog
from apps.blog.serializers import BlogCUDSerializer
from apps.common.views import AppModelCUDAPIViewSet


class BlogCUDAPIViewSet(AppModelCUDAPIViewSet):
    """
    ViewSet to handle the CUD operations for the `Blog` model.
    """

    serializer_class = BlogCUDSerializer
    queryset = Blog.objects.all()
