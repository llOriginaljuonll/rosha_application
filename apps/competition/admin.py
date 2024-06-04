from django.contrib import admin
from apps.competition.models import Competition

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    pass