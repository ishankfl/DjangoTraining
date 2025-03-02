from rest_framework import serializers
from .models import User

def age_validator(age):
    if age < 18:
        raise serializers.ValidationError("Age must be greater than 18")
    return age

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
        # fields =['id','username']
        extra_kwargs = {
            'age':{
                'validators':[age_validator]
            },
            'password':{
                'write_only':True,
                'required':True
            },
            'email':{
                'write_only':True
            }
            
        }