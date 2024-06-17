from apps.blog.models import Blog
from apps.common.serializers import AppWriteOnlyModelSerializer


class BlogCUDSerializer(AppWriteOnlyModelSerializer):
    """
    Serializer to handle the CUD operations for the `Blog` model.
    """

    class Meta(AppWriteOnlyModelSerializer.Meta):
        model = Blog
        fields = ["title", "content"]
