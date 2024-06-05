from django.contrib import admin
from apps.participant.models import Participant

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    pass