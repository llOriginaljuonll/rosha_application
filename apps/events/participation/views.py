from django.views.generic import DetailView, UpdateView, ListView, DeleteView
from django.views.generic.edit import FormMixin
from .models import Participation
from .forms import ParticipationForm
from apps.events.audition.models import Audition
from core.mixins import IsStaffMixin, IsActiveMixin
from django.urls import reverse_lazy


class ParticipationFormView(IsActiveMixin, DetailView, FormMixin):

    model = Audition
    form_class = ParticipationForm
    template_name = 'events/participation/participation_form.html'
    context_object_name = 'audition'

    def get_success_url(self) -> str:
        return reverse_lazy('participation:list')
    
    def get_context_data(self, **kwargs):
        context = super(ParticipationFormView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
    def post(self, *args, **kwargs):
        # เรียกใช้ self.get_object() เพื่อกำหนด self.object
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
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