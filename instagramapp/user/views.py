from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from instagramapp.models import User
from .serializers import UserSerializers,UserSerializers2
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password



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
        req.data['password'] = make_password(req.data['password'])
        serializer=UserSerializers2(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            



@api_view(['GET','PUT'])
def userDetails(req,pk):
    if req.method=="GET":
        user=User.objects.get(id=pk)
        serializers=UserSerializers(user,many=False)
        return Response(serializers.data)
    elif req.method=="PUT":
        try:
            user=User.objects.get(id=pk)
            follow=User.objects.get(id=req.data.get('follow'))
            test=follow
            user.following.add(test)
            user.save()
            follow.followers.add(user)
            follow.save()
            return Response("Done")
        except:
            return Response("Something went wrong")

@api_view(['PUT'])
def changePassword(req,pk):
    if req.method=="PUT":
        user=User.objects.get(id=pk)
        req.data['password'] = make_password(req.data['password'])
        seriliazer=UserSerializers2(user,data=req.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response("Password changeg")
        else:
            return Response({"msg":"something went wrong"})


@api_view(['POST'])
def login(req):
    if req.method=='POST':
        username=req.data['username']
        password=req.data['password']
        try:
            user=User.objects.get(username=username)
            if check_password(password,user.password):
                user=UserSerializers2(user,many=False)
                return Response({"message":"Logged in","data":user.data})
            else:
                return response({"message":"USERNAME OR PASSWORD DOES NOT EXIST"})
            

        except:
            return Response({"message":"USER DOES NOT EXIST"})




