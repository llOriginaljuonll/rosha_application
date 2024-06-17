from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from apps.competition.models import Competition
from apps.participant.models import Participant
from apps.participant.forms import ParticipantForm
from apps.referee.models import Score
from django.urls import reverse_lazy
from core.mixins import IsActiveMixin, IsEditorMixin
from django.contrib import messages
from django.shortcuts import redirect

class ParticipantListView(IsEditorMixin, ListView):

    model = Participant
    template_name = 'participants/participant_list.html'
    context_object_name = 'participants'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["score"] = Score.objects.filter(id=self.kwargs.get('id'))
        return context

    def get_queryset(self, *args, **kwargs):
        return Participant.objects.filter(competition__id=self.kwargs.get('pk')).order_by('score__average')
    

class ParticipandDetailView(DetailView):

    model = Participant
    object_name = 'participant'
    template_name = 'participants/participant_detail.html'
    context_object_name = 'participant'

    def handle_no_permission(self, request):
        messages.add_message(request, messages.ERROR, "You need higher permissions in order to access this page.")
        return redirect("competition:list")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR, "You need to be logged in in order to access this page.")
            return redirect("account_login")
        if request.user.is_editor or request.user.id == obj.user.id:
            pass
        else:
            return self.handle_no_permission(request)
        return super().dispatch(request, *args, **kwargs)


class ParticipantFormView(IsActiveMixin, DetailView, FormMixin):

    model = Competition
    form_class = ParticipantForm
    template_name = 'participants/participant_form.html'
    context_object_name = 'competition'

    def get_success_url(self) -> str:
        return reverse_lazy('competition:list')
    
    def get_context_data(self, **kwargs):
        context = super(ParticipantFormView, self).get_context_data(**kwargs)
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
    