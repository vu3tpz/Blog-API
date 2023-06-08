from django.db import models
from account.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now=True, blank=True)
    status = models.BooleanField(default=False)