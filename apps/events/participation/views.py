from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy

from .models import Participation
from .forms import ParticipationForm
from core.mixins import IsStaffMixin


class ParticipationCreateView(IsStaffMixin, CreateView):
    
    form_class = ParticipationForm
    template_name = 'events/participation/participation_form.html'
    success_url = reverse_lazy('participation:list')
    
class ParticipationUpdateView(IsStaffMixin, UpdateView):

    model = Participation
    form_class = ParticipationForm
    template_name = 'events/participation/participation_update.html'

    def get_success_url(self) -> str:
        return reverse_lazy('audition:list')
    
class ParticipationDeleteView(IsStaffMixin, DeleteView):

    model = Participation
    success_url = reverse_lazy("participation:list")

    """Overide get method for Creating DeleteView without templates_name"""
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

class ParticipationListView(IsActiveMixin, ListView):

    model = Participation
    template_name = 'events/participation/participation_list.html'
    context_object_name = 'participations'