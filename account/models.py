from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager

# Create your models here.
class Role(models.Model):
    """
    Model holds Roles like `Admin`, `User`, etc..
    """
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class Permission(models.Model):
    """
    Model holds Permissions like `Manage User`, `Manage Roles`, etc..
    """
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class Method(models.Model):
    """
    Model holds Methods like `GET`, `POST`, etc..
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RolePermission(models.Model):
    """
    This model act like a connecting points for `Role`, `Permissions`, `Methods`.
    """
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    method = models.ManyToManyField(Method)

class User(AbstractUser):
    """
    This model holds the `Basic Details` for authentication.
    """
    username = None
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(RolePermission, on_delete=models.SET_NULL, null=True)
    joined_on = models.TimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"