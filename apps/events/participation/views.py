from django.views.generic import DetailView, UpdateView
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
        return reverse_lazy('audition:list')
    
    def get_context_data(self, **kwargs):
        context = super(ParticipationFormView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
    def post(self, *args, **kwargs):
        
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('audition:list') 