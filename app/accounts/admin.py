from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2')}
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)

    list_display = ('username', 'email', 'first_name', 'last_name')
