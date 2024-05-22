from django.db import models
from accounts.models import User, CustomUser
from django.conf import settings
from django.db import migrations, models
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_complete = models.BooleanField(default=False, blank=True)

from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pages_profile')
    profile_image = models.CharField(max_length=100, choices=[
        ('hero1', 'Hero 1'),
        ('hero2', 'Hero 2'),
        ('hero3', 'Hero 3')
    ], default='hero1')

    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pages_userprofile')
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Migration(migrations.Migration):
    dependencies = [
        ('accounts', 'previous_migration_file'),  # Замените на имя последней миграции
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]