from django.urls import path
from .views import *

urlpatterns=[
path('register/', RegisterView.as_view(), name='register-view'),
path('login/', LoginView.as_view(), name='register-view'),
path('api/custom-token/', CustomTokenView.as_view(), name='custom-token-view'),
path('', ArticleCreateGetView.as_view(), name='article-view'),
path('data/<int:pk>/', ArticleUpdateDeleteEdit.as_view(), name='article-view'),
path('list-article-by-user', ListArticleByUser.as_view(), name='article-view'),

    
]