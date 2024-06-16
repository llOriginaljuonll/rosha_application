from django.contrib import admin
from apps.referee.models import Score

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass