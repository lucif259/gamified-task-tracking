from django.db import models
from accounts.models import CustomUser
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_complete = models.BooleanField(default=False, blank=True)