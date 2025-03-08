from django.contrib import admin
from django.urls import path
from .views import LoginView, UserRegiserView
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/login/',LoginView.as_view(), name='login-view'),
    path('api/register/',UserRegiserView.as_view(), name='login-view')
]
