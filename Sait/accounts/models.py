from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='accounts_profile')
    profile_image = models.CharField(max_length=100, choices=[
        ('hero1', 'Hero 1'),
        ('hero2', 'Hero 2'),
        ('hero3', 'Hero 3')
    ], default='hero1')

    def __str__(self):
        return self.user.username

class CustomUser(AbstractUser):

    def __str__(self):
        return f"{self.first_name}" + f"{self.last_name}"
