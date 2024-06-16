from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.common.managers import UserManager
from apps.common.models import COMMON_CHAR_FIELD_MAX_LENGTH, BaseModel


class User(AbstractUser, BaseModel):
    """
    This model holds the `Basic Details` for authentication.

    ********************* Model Fields *********************
        PK          - id
        Unique      - uuid, username, email
        FK          - created_by, modified_by, deleted_by
        Datetime    - created, modified, deleted
        Boolean     - is_active, is_deleted
        Char        - first_name, last_name, username, password
        Email       - email
    """

    username = None
    objects = UserManager()

    first_name = models.CharField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH)
    last_name = models.CharField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH)
    username = models.CharField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=COMMON_CHAR_FIELD_MAX_LENGTH)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
