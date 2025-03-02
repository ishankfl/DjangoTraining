from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=40)
    
    def __str__(self):
        return self.username
    