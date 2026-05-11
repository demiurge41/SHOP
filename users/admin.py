from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import ConfirmationCode, CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = [
        "id",
        "email",
        "phone_number",
        "birthdate",
        "is_active",
        "is_staff"
        ]
    

    list_editable = ["is_active"]
    ordering = ["email"]

    fieldsets = ((None, {"fields": (
        "email",
        "password",
        "phone_number",
        "birthdate",
        "is_active"
    )}),
    ("Important dates", {"fields": ("last_login",)}),
)


@admin.register(ConfirmationCode)
class ConfirmationCodeAdmin(admin.ModelAdmin):
    list_display = ["id", "code"]
