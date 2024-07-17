from django.urls import path
from apps.events.competition.views import CompetitionFormtView

urlpatterns = [
    path('form/', CompetitionFormtView.as_view(), name='form'),
]
