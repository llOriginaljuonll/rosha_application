from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.events.participation.models import Participation
from apps.events.participation.forms import ParticipationForm
from core.mixins import IsStaffMixin, IsActiveMixin
from django.urls import reverse_lazy

class ParticipationCreateView(IsStaffMixin, CreateView):

    model = Participation
    object_name = "participation"
    form_class = ParticipationForm
    template_name = 'events/participation/participation_form.html'

    def get_success_url(self) -> str:
        return reverse_lazy('audition:list') 