from rest_framework import serializers

from blog.models import Blog, Comment
from user.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content','created_at']
        
class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many = True, read_only = True)
    class Meta:
        model  = Blog
        fields = '__all__'
        read_only_fields = ['author','comments']