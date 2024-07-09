from django.urls import path
from . import views

app_name = "participant"

urlpatterns = [
    path('form/<slug>/<int:auditioner_id>', views.ParticipantFormView.as_view(), name='form'),
]
