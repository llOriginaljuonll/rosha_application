from django.views.generic import CreateView, DetailView, ListView, DeleteView
from django.views.generic.edit import FormMixin
from .models import Entrant
from .forms import EntrantForm
from django.contrib import messages
from django.urls import reverse_lazy
from core.mixins import IsActiveMixin, IsEditorMixin
from apps.events.competition.models import Competition
from django.shortcuts import redirect


class EntrantListView(IsEditorMixin, ListView):

    model = Entrant
    template_name = 'performer/entrants/entrant_list.html'
    context_object_name = 'entrants'

    def get_queryset(self,*args, **kwargs):
        return Entrant.objects.filter(compt__id=self.kwargs.get('pk'))


class EntrantCreateView(CreateView):

    model = Entrant
    form_class = EntrantForm
    template_name = 'performer/entrants/entrant_form.html'
    success_url = reverse_lazy("compt:compeition_list")

    def dispatch(self, request, *args, **kwargs):
        self.competition_id = self.kwargs.get("compeition_id")
        self.competition = Competition.objects.get(pk=self.competition_id)
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["competition"] = self.competition_id
        return context
    
    def form_valid(self,form):
        form.instance.audition = self.competition_id
        return super().form_valid(form)


class EntrantDetailView(DetailView):

    model = Entrant
    object_name = 'entrant'
    template_name = 'performer/entrants/entrant_detail.html'
    context_object_name = 'entrant'

    def handle_no_permission(self, request):
        messages.add_message(request, messages.ERROR, "You need higher permissions in order to access this page.")
        return redirect("/")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR, "You need to be logged in in order to access this page.")
            return redirect("account_login")
        if request.user.is_judge or request.user.id == obj.user.id:
            pass
        else:
            return self.handle_no_permission(request)
        return super().dispatch(request, *args, **kwargs)

class EntrantDeleteView(DeleteView):

    model = Entrant

    """Overide get method for Creating DeleteView without templates name"""
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('entrant:list', kwargs={"pk": self.get_object().compt.id})