

from django.urls import path
from . import views

# serverurl/home/home/
urlpatterns = [
    path('crud/',views.crud_task),
]
# task/crud/