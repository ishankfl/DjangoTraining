from django.contrib import admin
from .models import User  # Importing the User model

# Register the User model to make it visible in the admin panel
admin.site.register(User)


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'created_at')  # Columns shown in the admin panel
#     search_fields = ('name', 'email')  # Search bar functionality
#     list_filter = ('created_at',)  # Filters on the right panel

# admin.site.register(User, UserAdmin)  # Registering with custom settings


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'user',
]
