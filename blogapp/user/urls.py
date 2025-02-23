# from django.urls import path
# from . import views

# urlpatterns = [
#     # path('response/<int:id>/', views.home, name='home'),
#     # path('response/<int:id>/', views.home, name='home'),
#     path('home/response/<int:id>/<str:category>', views.home, name='home'),

# ]

# # http://127.0.0.1:8000/home/response/

from django.urls import path
from . import views

# serverurl/home/home/
urlpatterns = [
    # path('home/', views.rendering_first_template, name='home'),
    # path('extend/',views.call_extend,name='extend')
    # path('login/'),
    path('register/',views.register),
    path('login/',views.login)
]
#  http://127.0.0.1:8000/home/home/
#  http://127.0.0.1:8000/home/extend/