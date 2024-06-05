from django.views.generic import CreateView, ListView, DetailView
from apps.competition.models import Competition
from apps.competition.forms import CompetitionForm
from django.urls import reverse_lazy

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

class CompetitionDetailView(DetailView):

    model = Competition
    template_name = 'competition/competition_detail.html'
    context_object_name = 'competition'