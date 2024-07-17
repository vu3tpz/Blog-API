from apps.blog.models import Blog
from apps.common.serializers import AppReadOnlyModelSerializer, AppWriteOnlyModelSerializer, SimpleUserSerializer


class BlogCUDSerializer(AppWriteOnlyModelSerializer):
    """
    Serializer to handle the CUD operations for the `Blog` model.
    """

    class Meta(AppWriteOnlyModelSerializer.Meta):
        model = Blog
        fields = ["title", "content", "description"]


class BlogListSerializer(AppReadOnlyModelSerializer):
    """
    Serializer to handle the read operations for the `Blog` model.
    """

    created_by = SimpleUserSerializer()

    class Meta(AppReadOnlyModelSerializer.Meta):
        model = Blog
        fields = ["id", "uuid", "title", "content", "description", "status", "created", "created_by"]
