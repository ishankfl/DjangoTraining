from django.db import models

# Create your models here.
# Register your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    USER_TYPE=(
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    user_type = models.CharField(choices=USER_TYPE,max_length=100)

