# Generated by Django 4.0.6 on 2023-01-23 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0033_friendrequest_timestamp_userprofile_friends'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FriendRequest',
        ),
    ]