from rest_framework.serializers import ModelSerializer
from instagramapp.models import User

class UserSerializers(ModelSerializer):
    class Meta:
        model=User
        fields=['id','name','email','followers','following','profileImage','phoneNumber','username','password']
    