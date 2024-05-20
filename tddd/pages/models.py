from django.db import models
from accounts.models import CustomUser
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    is_complete = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.title} | {self.user.username if self.user else "Нет пользователя"}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'