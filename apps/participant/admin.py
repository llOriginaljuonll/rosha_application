from django.contrib import admin
from apps.participant.models import Participant
from apps.events.audition.models import Competition
from apps.referee.models import Score
from django.db import models
from django import forms



class ScoreInline(admin.StackedInline):
    model = Score
    classes = ["collapse"]

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    inlines = [ScoreInline]
    formfield_overrides = {
        models.TextField: {
            "widget": forms.Textarea(attrs={"rows": 4, "cols": 40})
        },
    }
    fieldsets = (
        (None, {
            "fields": (
                "name",
                "competition",
                "instrument",
                "song",
                "slip",
            )
        }),
        (
            ("Profile"), {
                "classes": ["collapse"],
                "fields": (
                    "nationality",
                     "birthdate",
                     "age",
                     "school",
                     "grade",
                     "personal_info",
                     "image",
                )
            }
        ),
        (
            ("Performance"), {
                "classes": ["collapse"],
                "fields": ("shorts_url",)
            }
        ),
        (
            ("Contact"), {
            "classes": ["collapse"],
            "fields": ("email", "phone"),
        },
        )
    )
    list_display = [
        "id",
        "name",
        "competition_name",
        "age",
        "school",
        "grade",
        "instrument",
        "nationality",
        "avg_score",
        "email",
        "phone",
    ]
    list_display_links = [
        "name",
    ]
    search_fields = [
        "name",
        "competition_name",
    ]
    list_filter = (
        "name",
        "competition__name",
        "school",
        "instrument",
        "nationality",
        "score__average"
    )

    def get_form(self, request, obj=None, **kwargs):
        """re-labelname in admin"""
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["slip"].label = "Proof of payment"
        return form

    def competition_name(self, obj):
        """Get competition name"""
        return obj.competition.name
    
    def avg_score(self, obj):
        """Get average score"""
        obj = obj.score.average
        if obj == 0:
            obj = "-"
        return obj
    
