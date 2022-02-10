from rest_framework.serializers import ModelSerializer
from instagramapp.models import Post
from rest_framework import serializers

class PostSerializers(ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
        depth=1

class PostSerializers2(ModelSerializer):
    image = serializers.ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model=Post
        fields = ("id", 'image', 'AboutImage', 'created', 'updated','user')