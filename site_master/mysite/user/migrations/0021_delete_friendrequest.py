# Generated by Django 4.0.6 on 2023-01-22 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_friendrequest_from_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FriendRequest',
        ),
    ]
