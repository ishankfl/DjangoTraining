from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User

from articles.serializers import CustomTokenSerializer, UserDetailsSerializer, ArticleSerilizers
from rest_framework.views  import APIView 
from rest_framework.response import *
from .models import Article

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
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

class ArticleCreateGetView(generics.ListCreateAPIView ): #retrive get/ #detroy delete
    permission_classes = [IsAuthenticated]

    queryset = Article.objects.all()
    serializer_class = ArticleSerilizers
    authentication_classes =[JWTAuthentication]

    # def get_queryset(self):
    #     return Article.objects.all()
    
class ListArticleByUser(generics.ListCreateAPIView):
    serializer_class = ArticleSerilizers
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print("in get")
        user = self.request.user
        print(user.email)
        print(self.request.data)
        return Article.objects.filter(author=user)


class ArticleUpdateDeleteEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerilizers
    
class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer