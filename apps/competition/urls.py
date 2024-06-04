from django.urls import path
from apps.competition import views

app_name = 'competition'

urlpatterns = [
    path('competition_form/', views.CompetitionCreateView.as_view(), name='form'),
]