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


class EntrantFormView(IsActiveMixin, DetailView, FormMixin):

    model = Competition
    form_class = EntrantForm
    template_name = 'performer/entrants/entrant_form.html'
    context_object_name = 'competition'

    def get_success_url(self) -> str:
        return reverse_lazy('compt:list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['pk'] = self.kwargs.get('pk')
        return kwargs
    
    def post(self, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        return super().form_valid(form)
        
    
    # get_form_kwargs คือ method ที่ทำหน้าที่ เพิ่มข้อมูลที่ถูกส่งไปยังฟอร์มของวิวนั้นๆ ได้

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['compt'] = self.get_object()
    #     return kwargs

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