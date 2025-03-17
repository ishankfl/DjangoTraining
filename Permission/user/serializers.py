from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
class ResgisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email','username','password','user_type']
        
    def create(self, data):
        user = User.objects.create_user(
        email = data['email'],
        username = data['username'],
        password = data['password'],
        user_type = data.get('user_type','user'))
        
        return user
