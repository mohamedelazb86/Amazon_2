# form

from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
class PostSerializers(serializers.ModelSerializer):
    user=UserSerializers()
    category=serializers.StringRelatedField()
    class Meta:
        model=Post
        fields='__all__'