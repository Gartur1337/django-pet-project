# Generated by Django 4.0.6 on 2023-01-23 21:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0032_alter_userprofile_options_userprofile_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendrequest',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='user.userprofile'),
        ),
    ]