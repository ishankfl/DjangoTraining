"""
URL configuration for newblog project.

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
from django.urls import path
from .views import RegisterView, AdminOnlyView
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('api/register/',RegisterView.as_view() ),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/admin-only/', AdminOnlyView.as_view())
    # path('admin/', admin.site.urls),
    # path('user/',include('user.urls'))
]
