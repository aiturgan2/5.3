from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'created_at')
    search_fields = ('phone_number',)
    list_filter = ('created_at',)