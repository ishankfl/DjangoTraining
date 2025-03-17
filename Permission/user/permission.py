from rest_framework.permissions import BasePermission

class IsAdminUserPermission(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type =='admin'

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type =='user'
   
        # return super().has_permission(request, view)