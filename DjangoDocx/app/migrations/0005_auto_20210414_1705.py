# Generated by Django 3.2 on 2021-04-14 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_profile_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='role',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
