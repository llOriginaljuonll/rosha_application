from django.views.generic import CreateView, ListView
from apps.competition.models import Competition
from apps.competition.forms import CompetitionForm
from core.mixins import IsStaffMixin
from django.urls import reverse_lazy

class CompetitionCreateView(IsStaffMixin, CreateView):

    model = Competition
    object_name = "competition"
    form_class = CompetitionForm
    template_name = 'competition/competition_form.html'

    def get_success_url(self) -> str:
        return reverse_lazy('competition:list')
    
class CompetitionListView(ListView):

    model = Competition
    template_name = 'competition/competition_list.html'
    context_object_name = 'competitions'