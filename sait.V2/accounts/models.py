from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# TODO: УДАЛЯЙ ПРИ МНЕ
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='accounts_profile')
    profile_image = models.CharField(max_length=100, choices=[
        ('hero1', 'Hero 1'),
        ('hero2', 'Hero 2'),
        ('hero3', 'Hero 3')
    ], default='hero1')

    def __str__(self):
        return self.user.username

# TODO: УДАЛЯЙ ПРИ МНЕ

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='accounts_userprofile')
    rating = models.IntegerField(default=0)

def __str__(self):
        return self.user.username


class CustomUser(AbstractUser):
    rating = models.IntegerField(default=0)
    profile_image = models.CharField(max_length=100, choices=[
        ('hero1.png', 'Hero 1'),
        ('hero2.png', 'Hero 2'),
        ('hero3.png', 'Hero 3')
    ], default='/static/hero1.png')

    def __str__(self):
        return f"{self.username}"


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title