from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length= 250)
    prfile_picture = models.ImageField(upload_to='user_image',null=True)
    address = models.CharField(max_length= 250,default='hi')
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
    
