from rest_framework.serializers import ModelSerializer
from instagramapp.models import Post

class PostSerializers(ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
        depth=1

class PostSerializers2(ModelSerializer):
    class Meta:
        model=Post
        fields = '__all__'