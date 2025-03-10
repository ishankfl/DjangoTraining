from django.shortcuts import render
from rest_framework import generics

from blog.models import Blog
from blog.serializers import BlogSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author = user)
        
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]
        
    # reverse('')
    
    # render (request,'lkjsdfj/lkdjfl')

class SingleBlogView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# def something(request, id)
api_view(['GET'])
def update_blogview(request, id):
    blog = Blog.objects.get(id=id)
    view_count = blog.view_count
    blog.view_count = view_count + 1
    print(blog.view_count)
    blog.save()
    print("Blog view count")
    return Response({'success':"Successfully updated"})