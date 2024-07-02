from apps.blog.models import Blog
from apps.blog.serializers import BlogCUDSerializer, BlogListSerializer
from apps.common.views import AppModelCUDAPIViewSet, AppModelListAPIViewSet


class BlogCUDAPIViewSet(AppModelCUDAPIViewSet):
    """
    ViewSet to handle the CUD operations for the `Blog` model.
    """

    serializer_class = BlogCUDSerializer
    queryset = Blog.objects.all()


class BlogListAPIViewSet(AppModelListAPIViewSet):
    """
    ViewSet to handle the list operations for the `Blog` model.
    """

    serializer_class = BlogListSerializer
    queryset = Blog.objects.all()
    search_fields = ["title"]
