from django.urls import path
from apps.participant import views

app_name = 'participant'

urlpatterns = [
    path('participant_form/<pk>', views.ParticipantFormView.as_view(), name='form'),
    path('participant_list/', views.ParticipantListView.as_view(), name='list'),
]
