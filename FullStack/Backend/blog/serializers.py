from rest_framework import serializers

from blog.models import Blog
from user.serializers import UserSerializer

class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model  = Blog
        fields = '__all__'
        read_only_fields = ['author']