from django.views.generic import TemplateView
from apps.events.audition.models import Audition
from apps.events.participation.models import Participation

class HomeView(TemplateView):

    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        auditions = Audition.objects.all()
        participations = Participation.objects.all()
        all_objs = [auditions, participations]
        events = []
        for objs in all_objs:
            for obj in objs:
                events.append(obj)
        context["events"] = events

        return context
