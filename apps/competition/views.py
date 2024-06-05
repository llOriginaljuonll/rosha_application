from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import FormMixin
from django.http import HttpResponseForbidden
from apps.competition.models import Competition
from apps.competition.forms import CompetitionForm
from apps.participant.forms import ParticipantForm
from django.urls import reverse_lazy, reverse

class CompetitionCreateView(CreateView):

    model = Competition
    form_class = CompetitionForm
    template_name = 'competition/competition_form.html'

    def get_success_url(self) -> str:
        return reverse_lazy('competition:list')
    
class CompetitionListView(ListView):

    model = Competition
    template_name = 'competition/competition_list.html'
    context_object_name = 'competitions'

class CompetitionDetailView(DetailView, FormMixin):

    model = Competition
    form_class = ParticipantForm
    template_name = 'participants/participant_form.html'
    context_object_name = 'competition'

    def get_success_url(self) -> str:
        return reverse_lazy('competition:list')
    
    def get_context_data(self, **kwargs):
        context = super(CompetitionDetailView, self).get_context_data(**kwargs)
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
    