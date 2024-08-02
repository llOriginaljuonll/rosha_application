from django.views.generic import UpdateView
from apps.referee.forms import ScoreForm, EntrantScoreForm
from django.urls import reverse_lazy

from apps.referee.models import Score, EntrantScore

    
class ScoreUpdateView(UpdateView):

    model = Score
    form_class = ScoreForm
    template_name = 'referee/score_update.html'

    def get_success_url(self):
        return reverse_lazy('auditioner:list', kwargs={"pk": self.get_object().auditioner.audition.id})
    
class EntrantScoreView(UpdateView):

    model = EntrantScore
    form_class = EntrantScoreForm
    template_name = 'referee/entrantscore.html'

    def get_success_url(self):
        return reverse_lazy('entrant:list', kwargs={"pk": self.get_object().entrant.compt.id})