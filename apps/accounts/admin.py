from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.accounts.models import CustomUser
from allauth.account.admin import EmailAddress
from django.contrib.auth.models import Group

# unregister
admin.site.unregister(Group)
admin.site.unregister(EmailAddress)

# register
admin.site.register(CustomUser)
