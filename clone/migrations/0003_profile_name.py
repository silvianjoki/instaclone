# Generated by Django 4.0.3 on 2022-04-04 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0002_remove_profile_followers_remove_profile_following_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=44, null=True),
        ),
    ]
