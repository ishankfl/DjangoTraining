from rest_framework import serializers
from django.contrib.auth.models import User

from articles.models import Article
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields =['is_superuser', 'is_staff']
    
    def create(self,validated_data):
        print(validated_data)
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

class ArticleSerilizers(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), write_only=True)
    
    authors_details = UserDetailsSerializer(source = 'author',read_only = True)
    # author details = 
    
    class Meta:
        model = Article
        fields = '__all__'

class CustomTokenSerializer(TokenObtainPairSerializer):
    def get_token(self,user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['what'] = "thisishomepage"
        return token
        