# Generated by Django 4.0.2 on 2022-02-18 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagramapp', '0013_user_token_alter_user_followers_alter_user_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='token',
        ),
    ]
