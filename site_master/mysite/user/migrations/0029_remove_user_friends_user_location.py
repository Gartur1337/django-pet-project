# Generated by Django 4.0.6 on 2023-01-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_friendrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='friends',
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
