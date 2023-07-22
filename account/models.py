from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.model import BaseModel

from .manager import CustomUserManager


# Create your models here.
class Method(BaseModel):
    """
    Model holds Methods like `GET`, `POST`, etc..
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Permission(BaseModel):
    """
    Model holds Permissions like `Manage User`, `Manage Roles`, etc..
    """

    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    method = models.ForeignKey(Method, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Role(BaseModel):
    """
    Model holds Roles like `Admin`, `User`, etc..
    """

    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    permission = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name


class User(AbstractUser):
    """
    This model holds the `Basic Details` for authentication.
    TODO: Need to upade User Model to store only deatils for basic details for `Authentication` like `Username`, `Email` and `Password`.
    """

    username = None
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    email = models.EmailField(unique=True)
    user_role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    joined_on = models.TimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
