# Generated by Django 4.0.3 on 2022-04-04 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0006_profile_followers_profile_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
