from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),  # Ensure 'fields' is specified correctly
    )

admin.site.register(CustomUser, CustomUserAdmin)
