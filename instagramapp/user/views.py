from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from instagramapp.models import User
from .serializers import UserSerializers,UserSerializers2
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
# from rest_framework_simplejwt.tokens import RefreshToken
from .generateToken import get_tokens_for_user


# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
# }

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def getUser(req): 
    print(req.user)
    if req.method=='GET':
        query = req.GET.get('name')
        # str1=int(req.GET.get('page'))     
        if query:
            users=User.objects.filter(Q(username__icontains=query)|
            Q(name__icontains=query))
        else:
            users=User.objects.all()
        serializers=UserSerializers(users,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    elif req.method=='POST':
        req.data['password'] = make_password(req.data['password'])
        serializer=UserSerializers2(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            



@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
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
            return Response("Done",status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def changePassword(req,pk):
    if req.method=="PUT":
        user=User.objects.get(id=pk)
        req.data['password'] = make_password(req.data['password'])
        seriliazer=UserSerializers2(user,data=req.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response("Password changeg",status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def login(req):
    if req.method=='POST':
        username=req.data['username']
        password=req.data['password']
        try:
            user=User.objects.get(username=username)
            if check_password(password,user.password):
                token=get_tokens_for_user(user)
                upadtedUser={"token":"Bearer "+token["access"]}
                # print(token['access'])
                user=UserSerializers2(user,many=False)
                upadtedUser.update(user.data)
                return Response({"message":"Logged in","data":upadtedUser},status=status.HTTP_200_OK)
            else:
                return Response({"message":"USERNAME OR PASSWORD DOES NOT EXIST"},status=status.HTTP_400_BAD_REQUEST)
            

        except:
            return Response({"message":"USER DOES NOT EXIST"},status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def validate_jwt_token(req):
    try:
        user=User.objects.get(id=req.user.id)
        print(req.headers['Authorization'],"================")
        userupdated={"token":req.headers['Authorization']}
        user=UserSerializers2(user)
        userupdated.update(user.data)
        return Response({"data":userupdated},status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
