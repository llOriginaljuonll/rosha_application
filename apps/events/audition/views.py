from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.events.audition.models import Audition
from apps.events.audition.forms import AuditionForm
from core.mixins import IsStaffMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect

class AuditionCreateView(IsStaffMixin, CreateView):
    model = Audition
    object_name = "audition"
    form_class = AuditionForm
    template_name = 'events/audition/audition_form.html'
    success_url = reverse_lazy('audition:list')

    def post(self, request, *args, **kwargs):
        min_age_values = request.POST.getlist('min_age[]')
        max_age_values = request.POST.getlist('max_age[]')
        type_values = request.POST.getlist('type[]')
        elig_values = request.POST.getlist('elig[]')

        # Filter out empty values
        filtered_min_ages = [age for age in min_age_values if age.strip()]
        filtered_max_ages = [age for age in max_age_values if age.strip()]
        filtered_types = [typ for typ in type_values if typ.strip()]
        filtered_eligs = [elig for elig in elig_values if elig.strip()]

        joined_min_ages = ', '.join(filtered_min_ages)
        joined_max_ages = ', '.join(filtered_max_ages)
        joined_types = ', '.join(filtered_types)
        joined_eligs = ', '.join(filtered_eligs)

        form = self.get_form()
        form.instance.min_age = joined_min_ages
        form.instance.max_age = joined_max_ages
        form.instance.type = joined_types
        form.instance.elig = joined_eligs

        if form.is_valid():
            audition_instance = form.save(commit=False)
            audition_instance.min_age = joined_min_ages
            audition_instance.max_age = joined_max_ages
            audition_instance.type = joined_types
            audition_instance.elig = joined_eligs
            audition_instance.save()

            # Redirect to the success URL
            return redirect(self.success_url)
        
        return self.form_invalid(form)

class AuditionUpdateView(IsStaffMixin, UpdateView):

    model = Audition
    form_class = AuditionForm
    template_name = 'events/audition/audition_update.html'
    success_url = reverse_lazy('audition:list')
    
class AuditionDeleteView(IsStaffMixin, DeleteView):

    model = Audition
    success_url = reverse_lazy("audition:list")

    """Overide get method for Creating DeleteView without templates_name"""
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class AuditionListView(ListView):

    model = Audition
    template_name = 'events/audition/audition_list.html'
    context_object_name = 'auditions'
    