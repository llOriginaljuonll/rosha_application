from django.contrib import admin
from .models import Participant

@admin.register(Participant)
class AuditionAdmin(admin.ModelAdmin):
    pass