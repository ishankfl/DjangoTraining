from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView, ListCreateAPIView

from user.models import User
from user.serializers import UserSerializer
# Create your views here.
class LoginView(TokenObtainPairView):
    pass

class UserRegiserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    