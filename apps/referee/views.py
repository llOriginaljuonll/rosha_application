from django.views.generic import UpdateView
from apps.referee.forms import ScoreForm
from django.urls import reverse_lazy

from apps.referee.models import Score

# class ScoreFormView(IsEditorMixin, DetailView, FormMixin):

#     model = Score
#     form_class = ScoreForm
#     template_name = 'referee/score_form.html'
#     context_object_name = 'score'

#     def get_success_url(self) -> str:
#         return reverse_lazy('participant:list', kwargs={"pk": self.get_object().competition.id})

#     def get_context_data(self, **kwargs):
#         context = super(ScoreFormView, self).get_context_data(**kwargs)
#         context['form'] = self.get_form()
#         return context
    
#     def post(self, *args, **kwargs):
        
#         form = self.get_form()
#         if form.is_valid():
#             form.save()
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
    
#     def form_valid(self, form):
#         return super().form_valid(form)
    
class ScoreUpdateView(UpdateView):

    model = Score
    form_class = ScoreForm
    template_name = 'referee/score_update.html'

    def get_success_url(self):
        return reverse_lazy('participant:list', kwargs={"pk": self.get_object().participant.competition.id})