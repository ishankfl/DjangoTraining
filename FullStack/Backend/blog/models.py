from django.db import models
from user.models import User
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length= 255)
    content = models.TextField()
    # image = models.ImageField(upload_to= 'blog_image', null=True)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='blogs/')
    
    def __str__(self):
        return self.author


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
