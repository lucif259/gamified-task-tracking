from django.contrib.auth.models import AbstractUser
from django.db import  models


class CustomUser(AbstractUser):
    point = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.username}" + f"{self.last_name}"
