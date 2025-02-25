

from django.urls import path
from . import views

# serverurl/home/home/
urlpatterns = [
    path('crud/',views.crud_task),# 127.0.0.1:8000/task/crud/
    path('signle_view/<int:id>/',views.signle_view),# 127.0.0.1:8000/task/crud/
    path('delete/<int:id>/',views.delete_view),# 127.0.0.1:8000/task/crud/
    path('update/',views.update_task), # 127.0.0.1:8000/task/update/
]
# task/crud/