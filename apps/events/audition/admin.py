from django.contrib import admin
from apps.events.models import Competition

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    pass