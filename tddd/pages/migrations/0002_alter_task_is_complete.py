# Generated by Django 4.1.3 on 2024-05-20 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_complete',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]