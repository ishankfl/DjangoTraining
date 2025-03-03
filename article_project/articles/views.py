from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User

from articles.serializers import UserDetailsSerializer, ArticleSerilizers
from rest_framework.views  import APIView 
from rest_framework.response import *
from .models import Article
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer

class LoginView(APIView):
    def post(self, request):
        user = request.data['username']
        password = request.data['password']

        try:
            user = User.objects.get(username = user)

        except:
            return Response({"error": "Invalid username"}, status=400)

        if user.check_password(password):
            return Response({"message": "Login successful"}, status=200)

        else:
            return Response({"error": "Invalid Password"}, status=400)

class ArticleCreateGetView(generics.ListAPIView): #retrive get/ #detroy delete
    queryset = Article.objects.all()
    serializer_class = ArticleSerilizers
    