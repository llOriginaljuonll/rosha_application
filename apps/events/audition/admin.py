from django.contrib import admin
from apps.events.audition.models import Audition

@admin.register(Audition)
class AuditionAdmin(admin.ModelAdmin):
    pass