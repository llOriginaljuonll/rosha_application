from django.urls import path
from apps.events.competition.views import CompetitionFormView

app_name="compt"

urlpatterns = [
    path('form/', CompetitionFormView.as_view(), name='form'),
]