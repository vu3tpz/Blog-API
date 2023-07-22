from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    """
    This model holds the details of like created_by, created_on and modified_on
    """

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
