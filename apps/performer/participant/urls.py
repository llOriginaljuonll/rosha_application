from django.urls import path
from . import views

app_name = "participant"

urlpatterns = [
    path('form/<int:pk>', views.ParticipantFormView.as_view(), name='form'),
]
