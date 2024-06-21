from django.views.generic import UpdateView
from apps.referee.forms import ScoreForm
from django.urls import reverse_lazy

from apps.referee.models import Score

    
class ScoreUpdateView(UpdateView):

    model = Score
    form_class = ScoreForm
    template_name = 'referee/score_update.html'

    def get_success_url(self):
        return reverse_lazy('participant:list', kwargs={"pk": self.get_object().participant.competition.id})