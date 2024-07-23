from django.urls import path
from apps.events.competition.views import ComptFormView, ComptListView

app_name="compt"

urlpatterns = [
    path('form/', CompetitionFormView.as_view(), name='form'),
]
