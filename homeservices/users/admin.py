# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name', 'first_name', 'last_name', 'profile_photo')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name'),
        }),
    )
    list_display = ('email', 'name', 'is_staff')
    search_fields = ('email', 'name', 'first_name', 'last_name')
    ordering = ('email',)
    
    # This makes the profile photo clickable
    readonly_fields = ('profile_photo_preview',)
    
    def profile_photo_preview(self, obj):
        if obj.profile_photo:
            return format_html('<a href="{0}" target="_blank"><img src="{0}" width="150" style="border-radius:50%" /></a>', obj.profile_photo)
        return "No photo"
    profile_photo_preview.short_description = 'Profile Photo Preview'

admin.site.register(CustomUser, CustomUserAdmin)