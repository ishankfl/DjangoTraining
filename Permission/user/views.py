from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from user.models import User
from user.serializers import ResgisterSerializer
from rest_framework.permissions import IsAuthenticated
from .permission import  IsAdminUserPermission
from rest_framework.response import Response

# Create your views here.
class RegisterView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = ResgisterSerializer

class AdminOnlyView(APIView):
    
    permission_classes = [IsAuthenticated,IsAdminUserPermission ]
    
    def get(self, request):
        return Response({"message": "Welcome Admin"})