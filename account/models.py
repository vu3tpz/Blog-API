from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(_("Email Field"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =[]

    object = CustomUserManager()

    def __str__(self):
        return self.email