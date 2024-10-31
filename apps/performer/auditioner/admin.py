from django.contrib import admin
from apps.performer.auditioner.models import Auditioner
from apps.referee.models import Score
from django.db import models
from django import forms

# admin.site.register(PerformResult)

class ScoreInline(admin.StackedInline):
    model = Score
    classes = ["collapse"]

@admin.register(Auditioner)
class AuditionerAdmin(admin.ModelAdmin):
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
                "audition",
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
                     "image",
                )
            }
        ),
        (
            ("Performance"), {
                "classes": ["collapse"],
                "fields": ("shorts_url", "shorts_video")
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
        "audition_name",
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
        # "audition_name",
    ]
    list_filter = (
        "name",
        "audition__name",
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

    def audition_name(self, obj):
        """Get audition name"""
        return obj.audition.name
    
    def avg_score(self, obj):
        """Get average score"""
        obj = obj.score.average
        if obj == 0:
            obj = "-"
        return obj
    
