from rest_framework import serializers

from user.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # write_only_fields = 
        read_only_fields =  ['is_superuser', 'is_staff', 'is_active', 'last_login','groups','user_permissions']
    
    def create(self, data):
        # data = {'user':"ishan", 'lastname'='kafle'}
        # **data = (user=ishan,lastname=kafle)
        user = User(**data)
        user.set_password(data['password'])
        user.save()
        return user
        
        # User ({username = isna, email = ishan})