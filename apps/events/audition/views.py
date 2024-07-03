from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.events.audition.models import Competition
from apps.events.audition.forms import CompetitionForm
from core.mixins import IsStaffMixin, IsActiveMixin
from django.urls import reverse_lazy

class CompetitionCreateView(IsStaffMixin, CreateView):

    model = Competition
    object_name = "competition"
    form_class = CompetitionForm
    template_name = 'competition/competition_form.html'

    def get_success_url(self) -> str:
        return reverse_lazy('competition:list')

class CompetitionUpdateView(IsStaffMixin, UpdateView):

    model = Competition
    form_class = CompetitionForm
    template_name = 'competition/competition_update.html'

    def get_success_url(self) -> str:
        return reverse_lazy('competition:list')
    
class CompetitionDeleteView(IsStaffMixin, DeleteView):

    model = Competition
    success_url = "/"

    """Overide get method for Creating DeleteView without templates name"""
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class CompetitionListView(IsActiveMixin, ListView):

    model = Competition
    template_name = 'competition/competition_list.html'
    context_object_name = 'competitions'