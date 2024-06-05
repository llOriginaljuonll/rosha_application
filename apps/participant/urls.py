from django.urls import path
from apps.participant import views

app_name = 'participant'

urlpatterns = [
    path('participant_form/<pk>', views.ParticipantFormView.as_view(), name='form')
]
