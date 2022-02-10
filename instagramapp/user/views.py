from rest_framework.decorators import api_view
from rest_framework.response import Response
from instagramapp.models import User
from .serializers import UserSerializers
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q


@api_view(['GET','POST'])
def getUser(req):
    if req.method=='GET':
        query = req.GET.get('name')
        if query:
            users=User.objects.filter(Q(username__icontains=query)|
            Q(name__icontains=query))
        else:
            users=User.objects.all()
        serializers=UserSerializers(users,many=True)
        return Response(serializers.data)
    elif req.method=='POST':
        print(req.data)
        serializer=UserSerializers(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error":"some error occured"})



@api_view(['GET'])
def userDetails(req,pk):
    user=User.objects.get(id=pk)
    serializers=UserSerializers(user,many=False)

    return Response(serializers.data)

@api_view(['POST'])
def login(req):
    if req.method=='POST':
        print(req.data)
        username='aquib12'
        password='123'
        try:
            user=User.objects.get(username=username)
            print(user)
        except:
            return Response({"message":"USER DOES NOT EXIST"})
        user=authenticate(req,username=username,password=password)
        if user is not None:
            login(req,user)
            return Response(user,"login successful")
        else:
            print(user)
            return Response({"message":"username and passowrd does not exist"})



