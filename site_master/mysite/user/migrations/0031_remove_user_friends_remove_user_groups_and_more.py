# Generated by Django 4.0.6 on 2023-01-23 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0030_remove_user_location_user_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Пользователь'},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='FriendRequest',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]