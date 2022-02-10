from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
    
class User(AbstractUser):
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(unique=True,null=True)
    username=models.CharField(unique=True,max_length=20,null=True)
    phoneNumber=models.IntegerField(null=True)
    profileImage=models.ImageField(default="avatar.svg",null=True)
    followers=models.ManyToManyField("self", blank=True)
    following=models.ManyToManyField("self", blank=True)

    def __str__(self):
        return str(self.username)


    
class Post(models.Model):
    image=models.ImageField(null=True)
    AboutImage=models.TextField(max_length=400,null=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering=['-updated','-created']
    
    def __str__(self):
        return self.AboutImage
