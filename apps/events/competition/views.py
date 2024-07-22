from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import CompetitionForm

class CompetitionFormView(FormView):
    template_name = 'events/competition/comp_form.html'
    form_class = CompetitionForm
    success_url = reverse_lazy('audition:list')

    def form_valid(self, form):
        elig_objs = self.request.POST.getlist("eligible") 
        elig = {
            "elig": elig_objs,
        }
        instr_objs = self.request.POST.getlist("type")
        instr_types = {
            "type": instr_objs,
        }
        competition = form.save(commit=False)
        competition.elig = elig
        competition.instr_type = instr_types
        competition.save()
        return super().form_valid(form)
