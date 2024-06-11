from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from apps.referee.models import Score
from apps.participant.models import Participant
from apps.referee.forms import ScoreForm
from django.urls import reverse_lazy

class ScoreFormView(DetailView, FormMixin):

    model = Participant
    form_class = ScoreForm
    template_name = 'referee/score_form.html'
    context_object_name = 'participant'

    def get_success_url(self) -> str:
        return reverse_lazy('competition:list')
    
    def get_context_data(self, **kwargs):
        context = super(ScoreFormView, self).get_context_data(**kwargs)
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