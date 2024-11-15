from django.urls import path
from .views import HallCreateView

app_name = "hall"

urlpatterns = [
    path("hall_form", HallCreateView.as_view(), name="hall-form")
]
