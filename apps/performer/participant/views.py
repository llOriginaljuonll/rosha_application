from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from core.mixins import IsActiveMixin
from apps.events.participation.models import Participation
from apps.performer.participant.forms import ParticipantForm
from apps.performer.auditioner.models import Auditioner
from django.urls import reverse_lazy

from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

class ParticipantFormView(IsActiveMixin, UpdateView):  # ใช้ UpdateView แทน DetailView
    model = Participation
    form_class = ParticipantForm
    template_name = 'performer/participants/participant_form.html'
    context_object_name = 'participation'

    def get_success_url(self) -> str:
        return reverse_lazy('participation:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # เพิ่มฟอร์มใน context
        return context

    
    # def get_context_data(self, **kwargs):
    #     context = super(ParticipantFormView, self).get_context_data(**kwargs)
    #     context['auditioner_obj'] = Auditioner.objects.get(pk=self.kwargs["auditioner_id"])
    #     context['form'] = self.get_form()
    #     return context