from typing import Any
from django.views.generic import TemplateView
from apps.events.audition.models import Audition
from apps.events.participation.models import Participation

class HomeView(TemplateView):

    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["auditions"] = Audition.objects.all()
        context["participations"] = Participation.objects.all()

        return context