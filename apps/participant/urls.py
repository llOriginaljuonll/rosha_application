from django.urls import path
from apps.participant import views

app_name = 'participant'

urlpatterns = [
    path('<str:pk>', views.ParticipantListView.as_view(), name='list'),
    path('detail/<int:pk>', views.ParticipantDetailView.as_view(), name='detail'),
    path('form/<pk>', views.ParticipantFormView.as_view(), name='form'),
    path('update/<pk>', views.ParticipantUpdateView.as_view(), name='update')
]
