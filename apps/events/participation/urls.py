from django.urls import path
from apps.events.participation.views import ParticipationCreateView

app_name = "participation"

urlpatterns = [
    path('form/', ParticipationCreateView.as_view(), name="form"),
]
