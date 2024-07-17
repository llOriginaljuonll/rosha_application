from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import CompetitionForm

class CompetitionFormtView(FormView):
    template_name = 'events/competition/comp_form.html'
    form_class = CompetitionForm
    success_url = reverse_lazy('audition:form')

    def form_valid(self, form):
        elig_objs = self.request.POST.getlist("elig") 
        elig = {
            "elig": elig_objs,
        }
        intr_types = self.request.POST.getlist("type")
        intr_type = {
            "type": intr_types
        }
        competition = form.save(commit=False)
        competition.elig = elig
        competition.intr_type = intr_type
        competition.save()
        return super().form_valid(form)
