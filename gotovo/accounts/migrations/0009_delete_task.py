# Generated by Django 4.1.3 on 2024-05-24 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_task'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]