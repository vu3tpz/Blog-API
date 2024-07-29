from rest_framework.decorators import action

from apps.access.config import UserTypeChoices
from apps.blog.config import BlogStatusChoices
from apps.blog.models import Blog
from apps.blog.serializers import BlogCUDSerializer, BlogListSerializer
from apps.common.views import AppAPIView, AppModelCUDAPIViewSet, AppModelListAPIViewSet


class BlogCUDAPIViewSet(AppModelCUDAPIViewSet):
    """
    ViewSet to handle the CUD operations for the `Blog` model.
    """

    serializer_class = BlogCUDSerializer
    queryset = Blog.objects.all()


class BlogListAPIViewSet(AppModelListAPIViewSet):
    """
    ViewSet to handle the list operations for the `Blog` model for authenticated user.
    """

    serializer_class = BlogListSerializer
    queryset = Blog.objects.all()
    search_fields = ["title"]
    filterset_fields = ["status"]

    def get_queryset(self):
        """Queryset to handle the list based on the user type."""

        user = self.get_user()
        queryset = super().get_queryset()
        if user.type == UserTypeChoices.user:
            return queryset.filter(created_by=user)
        elif user.type == UserTypeChoices.admin:
            return queryset
        return queryset.none()


class BlogStatusAPIViewSet(AppModelListAPIViewSet):
    """
    Handles the status of a Blog.
    """

    serializer_class = BlogCUDSerializer
    queryset = Blog.objects.all()

    # @action(detail=True, methods=["post"])
    # def transition_to_review(self, request, pk=None):
    #     blog = self.get_object()
    #     BlogWorkflow().draft(blog)
    #     blog.save()
    #     return self.send_response({"status": "Transitioned to review"})
