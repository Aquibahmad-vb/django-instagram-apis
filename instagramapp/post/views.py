from rest_framework.decorators import api_view
from rest_framework.response import Response
from instagramapp.models import Post
from .serializers import PostSerializers


@api_view(['POST','GET'])
def getPost(req):
    if req.method=='GET':
        Posts=Post.objects.all()
        serializers=PostSerializers(Posts,many=True)
        return Response(serializers.data)
    elif req.method=='POST':
        print(req.data)
        serializer=PostSerializers(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            # print(serializer.data)
            return Response(serializer.errors)



@api_view(['GET','PUT','DELETE'])
def PostDetails(req,pk):
    if req.method=='GET':
        post=Post.objects.get(id=pk)
        serializers=PostSerializers(post,many=False)
        return Response(serializers.data)
    elif req.method=='PUT':
        post=Post.objects.get(id=pk)
        serializer=PostSerializers(post,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif req.method=="DELETE":
        post=Post.objects.get(id=pk)
        if post:
            post.delete()
            return Response({"POST DELETED "})



