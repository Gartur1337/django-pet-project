# Generated by Django 4.0.6 on 2023-01-23 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0035_friendrequest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Пользователь'},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]