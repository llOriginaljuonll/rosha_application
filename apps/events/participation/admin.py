from django.contrib import admin
from apps.events.participation.models import Participation

@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    pass
