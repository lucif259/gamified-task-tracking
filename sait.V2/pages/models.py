from django.db import models
from accounts.models import User, CustomUser
from django.conf import settings
from django.db import migrations, models
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_complete = models.BooleanField(default=False, blank=True)
    rating = models.IntegerField(default=0)


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


def get_user_raiting(user_id: int):
    tasks = Task.objects.filter(is_complete=True, user_id=user_id)
    raitings = (task.rating for task in tasks)
    sum_raiting = sum(raitings)
    return sum_raiting


def set_task_to_user(task_id: int, user: CustomUser):
    task = Task.objects.get(id=task_id)
    task.user = user
    task.save()


def get_unused_tasks():
    tasks = Task.objects.filter(user=None)
    return tasks


def get_user_tasks(user_id: int):
    tasks = Task.objects.filter(user_id=user_id)
    return tasks