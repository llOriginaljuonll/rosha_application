from django.views.generic import CreateView
from apps.competition.models import Competition
from apps.competition.forms import CompetitionForm
from django.urls import reverse_lazy

class CompetitionCreateView(CreateView):

    model = Competition
    form_class = CompetitionForm
    template_name = 'competition/competition_form.html'

    def get_success_url(self) -> str:
        return reverse_lazy('competition:form')