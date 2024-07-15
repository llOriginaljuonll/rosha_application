from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from apps.events.audition.models import Audition
from apps.performer.auditioner.models import Auditioner
from apps.performer.auditioner.forms import AuditionerForm, PerformResultForm
from apps.referee.models import Score
from django.urls import reverse_lazy
from core.mixins import IsActiveMixin, IsEditorMixin, IsStaffMixin
from django.contrib import messages
from django.shortcuts import redirect

class AuditionerListView(IsEditorMixin, ListView, FormMixin):

    model = Auditioner
    form_class = PerformResultForm
    template_name = 'performer/auditioners/auditioner_list.html'
    context_object_name = 'auditioner_objects'

    def get_success_url(self) -> str:
        return reverse_lazy('audition:list')
    
    def get_queryset(self, *args, **kwargs):
        return Auditioner.objects.filter(audition__id=self.kwargs.get('pk')).order_by('score__average')
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['auditioners'] = Auditioner.objects.all()
        context['forms'] = {auditioner.id: PerformResultForm(initial={'auditioner': auditioner}) for auditioner in context['auditioners']}
        for auditioner in context['auditioners']:
            auditioner = {auditioner.id: PerformResultForm(initial={'auditioner': auditioner})}
            print(auditioner)
        context["score"] = Score.objects.filter(id=self.kwargs.get('id'))
        return context





        # auditioners = Auditioner.objects.all()
        # for auditioner in auditioners:
        #     result_form = PerformResultForm(auditioner=auditioner.name)
        # print(self.kwargs.get())

        # context["form"] = result_form
        # auditioner_id = self.request.GET.get("auditioner_id")
        # context["form"] = self.get_form()
        # form = self.form_class(initial=auditioner_id)
        # context["form"] = form
        

    
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['audit_id'] = self.kwargs['audit_id']
    #     return kwargs
    
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     auditioners = Auditioner.objects.all()
    #     for auditioner in auditioners:
    #         kwargs["auditioner"] = auditioner
    #     return kwargs

    def post(self, request, *args, **kwargs):
        
        form = PerformResultForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            context = self.get_context_data()
            writer_id = int(request.POST.get('auditioner'))
            context['forms'][writer_id] = form
            return self.render_to_response(context)

    
class AllAuditionerLisview(IsStaffMixin, ListView):

    model = Auditioner
    template_name = "performer/auditioners/auditioner_all_list.html"
    context_object_name = "auditioners"
    ordering = ["-id"]

class AuditionerDetailView(DetailView):

    model = Auditioner
    object_name = 'auditioner'
    template_name = 'performer/auditioners/auditioner_detail.html'
    context_object_name = 'auditioner'

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


class AuditionerFormView(IsActiveMixin, DetailView, FormMixin):

    model = Audition
    form_class = AuditionerForm
    template_name = 'performer/auditioners/auditioner_form.html'
    context_object_name = 'audition'

    def get_success_url(self) -> str:
        return reverse_lazy('audition:list')
    
    def get_context_data(self, **kwargs):
        context = super(AuditionerFormView, self).get_context_data(**kwargs)
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
    
class AuditionerUpdateView(UpdateView):

    model = Auditioner
    form_class = AuditionerForm
    template_name = 'performer/auditioners/auditioner_update.html'

    def handle_no_permission(self, request):
        messages.add_message(request, messages.ERROR, "You need higher permissions in order to access this page.")
        return redirect("/")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not request.user.is_authenticated:
            messages.add_message(request, messages.ERROR, "You need to be logged in in order to access this page.")
            return redirect("account_login")
        if request.user.is_staff or request.user.id == obj.user.id:
            pass
        else:
            return self.handle_no_permission(request)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('auditioner:detail', kwargs={"pk": self.get_object().id})

class AuditionerDeleteView(DeleteView):

    model = Auditioner

    """Overide get method for Creating DeleteView without templates name"""
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('auditioner:list', kwargs={"pk": self.get_object().competition.id})