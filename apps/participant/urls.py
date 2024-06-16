from django.urls import path
from apps.participant import views

app_name = 'participant'

urlpatterns = [
    path('<str:pk>', views.ParticipantListView.as_view(), name='list'),
    path('participant_detail/<int:pk>', views.ParticipandDetailView.as_view(), name='detail'),
    path('participant_form/<pk>', views.ParticipantFormView.as_view(), name='form'),
]
