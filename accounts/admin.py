
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib import admin
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
    ("Additional information", {"fields": ("role",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
    ("Additional information", {"fields": ("role",)}),
    )

    lisT_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_staff",
    )