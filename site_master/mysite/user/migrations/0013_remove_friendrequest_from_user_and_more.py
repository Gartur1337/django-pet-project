# Generated by Django 4.0.6 on 2023-01-22 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_userprofile_options_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='friendrequest',
            name='to_user',
        ),
    ]
