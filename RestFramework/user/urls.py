"""
URL configuration for restapipractise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
# from .views import *
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserModelViewSet
routers = DefaultRouter()
routers.register(r'users',UserViewSet, basename='users')
routers.register(r'model-users',UserModelViewSet, basename='model-users')

urlpatterns = [
    path('viewset-example/', include(routers.urls))
    # path('items/', item_list),
    # path('user/', user_auth)
    
]
