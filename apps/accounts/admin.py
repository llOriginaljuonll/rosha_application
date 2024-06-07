from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.accounts.models import CustomUser
from allauth.account.admin import EmailAddress

admin.site.unregister(EmailAddress)
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_editor",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    ordering = ( "date_joined", "last_login")
    list_display = [
        "id",
        "username",
        "is_active",
        "is_editor",
        "is_staff",
        "is_superuser",
        "date_joined",
        "last_login",
    ]
    list_display_links = ["username",]
    search_fields = ["username", ]
    list_filter = (
        "is_superuser",
        "is_editor",
        "is_staff",
        "is_active",
        "date_joined",
        "last_login",
    )
    default_selected_columns = [
        "id",
        "username",
        "is_active",
        "is_editor",
        "is_staff",
        "is_superuser",
        "date_joined",
        "last_login",
    ]
