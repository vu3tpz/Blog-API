from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.common.managers import UserManager
from apps.common.models import BaseModel


class User(AbstractUser, BaseModel):
    """
    This model holds the `Basic Details` for authentication.
    TODO: Need to upade User Model to store only deatils for basic details for `Authentication` like `Username`, `Email` and `Password`.
    """

    username = None
    objects = UserManager()

    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
