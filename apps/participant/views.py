from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from apps.competition.models import Competition
from apps.participant.models import Participant
from apps.participant.forms import ParticipantForm
from django.urls import reverse_lazy
from core.mixins import IsStaffMixin

class ParticipantListView(IsStaffMixin, ListView):

    model = Participant
    template_name = 'participants/participant_list.html'
    context_object_name = 'participants'

    ordering = ['-pk']

class ParticipandDetailView(IsStaffMixin, DetailView):

    model = Participant
    object_name = 'participant'
    template_name = 'participants/participant_detail.html'
    context_object_name = 'participant'

class ParticipantFormView(DetailView, FormMixin):

    model = Competition
    form_class = ParticipantForm
    template_name = 'participants/participant_form.html'
    context_object_name = 'competition'

    def get_success_url(self) -> str:
        return reverse_lazy('competition:list')
    
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