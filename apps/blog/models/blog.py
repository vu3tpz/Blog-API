from django.db import models

from apps.blog.config import BlogStatusChoices
from apps.common.models import COMMON_CHAR_FIELD_MAX_LENGTH, BaseModel


class Blog(BaseModel):
    """
    This model holds the `Basic Details` for Blog.

    ********************* Model Fields *********************
        PK          - id
        Unique      - uuid
        FK          - created_by, modified_by, deleted_by
        Datetime    - created, modified, deleted
        Boolean     - is_active, is_deleted
        Char        - title
        Text        - content, description
        Choice      - status
    """

    # Char field
    title = models.CharField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH)

    # Text field
    description = models.TextField()
    content = models.TextField()

    # Choice field
    status = models.CharField(
        max_length=COMMON_CHAR_FIELD_MAX_LENGTH, choices=BlogStatusChoices, default=BlogStatusChoices.under_review
    )

    class Meta:
        default_related_name = "related_blog"
