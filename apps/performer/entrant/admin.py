from django.contrib import admin
from .models import Entrant
# Register your models here.
@admin.register(Entrant)
class EntrantAdmin(admin.ModelAdmin):
    pass