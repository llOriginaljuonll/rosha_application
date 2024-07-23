from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, UpdateView, DeleteView
from core.mixins import IsActiveMixin, IsStaffMixin
from .forms import CompetitionForm
from .models import Competition

class ComptFormView(FormView):
    template_name = 'events/competition/compt_form.html'
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
    
class ComptListView(IsActiveMixin, ListView):

    model = Competition
    template_name = 'events/competition/compt_list.html'
    context_object_name = 'competitions'

class ComptUpdateView(IsStaffMixin, UpdateView):

    model = Competition
    form_class = CompetitionForm
    template_name = 'events/competition/compt_update.html'

    def get_success_url(self) -> str:
        return reverse_lazy('compt:list')
    
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
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)

        context['descr_patment'] = self.object.descr_payment
        context['eligs'] = (self.object.elig or {}).get('elig', [])
        context['types'] = (self.object.instr_type or {}).get('type', [])
        return context
    
class ComptDeleteView(IsStaffMixin, DeleteView):

    model = Competition
    success_url = reverse_lazy("compt:list")

    """Overide get method for Creating DeleteView without templates_name"""
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


    
