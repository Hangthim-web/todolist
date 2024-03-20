from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from accounts.models import CustomUser


# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        "gender",
        "age",
        "address",
        "is_staff",
    ]

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("gender", "age", "address",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("gender", "age", "address",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
