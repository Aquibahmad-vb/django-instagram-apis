# Generated by Django 4.0.2 on 2022-02-09 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagramapp', '0002_post_user_followers_user_following_user_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
