from django.db import models
from accounts.models import User, CustomUser
from django.conf import settings
from django.db import migrations, models
from django.contrib.auth import get_user_model
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


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

class TaskResponse(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response for Task {self.task} by {self.user}"
