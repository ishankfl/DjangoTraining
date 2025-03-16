from django.shortcuts import render
from rest_framework import generics

from blog.models import Blog, Comment
from blog.serializers import BlogSerializer, CommentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import CursorPagination, LimitOffsetPagination
# Create your views here.

class BlogPagination(CursorPagination):
    page_size = 6
    page_query_param = 'page_no' 
    max_page_size = 50

class LimitOffSetPagniateBlog(LimitOffsetPagination):
    default_limit = 5
    max_limit = 5
    
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class =LimitOffSetPagniateBlog
    
    
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
    queryset = Blog.objects.prefetch_related('comments').all()
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

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    # serializer = CommentSerializer(data)
    # serializer.save()
    def perform_create(self, serializer):
        try:
            blog_id = self.kwargs.get('blog_id')
            blog = Blog.objects.get(id = blog_id)
            serializer.save(blog = blog)
            
        except Blog.DoesNotExist:
            print("Blog not found")
        # return super().perform_create(serializer)
    
    