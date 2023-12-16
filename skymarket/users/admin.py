from django.contrib import admin
from django.contrib.admin import ModelAdmin
from users.models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_active', 'email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    exclude = ('password', 'last_login')
