# view api

from . import serializers
from rest_framework import generics
from .models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view

# create crud by cbv

class PostApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=serializers.PostSerializers

class PostDetailApi(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=serializers.PostSerializers


# create api by fuction
@api_view(['GET'])
def postapiapi(request):
    post=Post.objects.all()
    mydata=serializers.PostSerializers(post,many=True).data
    return Response({'data':mydata})

class postall(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=serializers.PostSerializers