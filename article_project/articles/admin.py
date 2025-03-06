from django.contrib import admin
from articles.models import Article

class ArticleCustomAdminView(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')
    search_fields = ('title','created_at')
    list_filter = ('created_at',)
admin.site.register(Article, ArticleCustomAdminView)