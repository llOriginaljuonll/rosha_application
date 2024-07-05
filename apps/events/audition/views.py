from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.events.audition.models import Audition
from apps.events.audition.forms import AuditionForm
from core.mixins import IsStaffMixin, IsActiveMixin
from django.urls import reverse_lazy
from apps.events.participation.models import Participation

class AuditionCreateView(IsStaffMixin, CreateView):

    model = Audition
    object_name = "audition"
    form_class = AuditionForm
    template_name = 'events/audition/audition_form.html'

    def get_success_url(self) -> str:
        return reverse_lazy('audition:list')

class AuditionUpdateView(IsStaffMixin, UpdateView):

    model = Audition
    form_class = AuditionForm
    template_name = 'events/audition/audition_update.html'

    def get_success_url(self) -> str:
        return reverse_lazy('audition:list')
    
class AuditionDeleteView(IsStaffMixin, DeleteView):

    model = Audition
    success_url = "/"

    """Overide get method for Creating DeleteView without templates_name"""
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class AuditionListView(IsActiveMixin, ListView):

    model = Audition
    template_name = 'events/audition/audition_list.html'
    context_object_name = 'auditions'
    