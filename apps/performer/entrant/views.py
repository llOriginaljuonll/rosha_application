from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormMixin
from .models import Entrant
from .forms import EntrantForm
from django.urls import reverse_lazy
from core.mixins import IsActiveMixin
from apps.events.competition.models import Competition

class EntrantFormView(IsActiveMixin, DetailView, FormMixin):

    model = Competition
    form_class = EntrantForm
    template_name = 'performer/entrant/entrant_form.html'
    context_object_name = 'competition'

    def get_success_url(self) -> str:
        return reverse_lazy('compt:list')
    
    def get_context_data(self, **kwargs):
        context = super(EntrantFormView, self).get_context_data(**kwargs)
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