from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from core.mixins import IsActiveMixin
from apps.events.participation.models import Participation
from apps.performer.participant.forms import ParticipantForm
from django.urls import reverse_lazy

class ParticipantFormView(IsActiveMixin, DetailView, FormMixin):

    model = Participation
    form_class = ParticipantForm
    template_name = 'performer/participants/participant_form.html'
    context_object_name = 'participation'

    def get_success_url(self) -> str:
        return reverse_lazy('audition:list')
    
    def get_context_data(self, **kwargs):
        context = super(ParticipantFormView, self).get_context_data(**kwargs)
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