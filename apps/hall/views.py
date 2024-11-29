from django.views.generic import CreateView
from .models import Hall
from .forms import HallForm

from django.urls import reverse_lazy
from django.utils.http import urlencode


class HallCreateView(CreateView):

    model = Hall
    form_class = HallForm
    template_name = "hall/hall_form.html"
    
    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url:
            return f"{next_url}?{urlencode({'created': 'true'})}"
        return reverse_lazy("home")