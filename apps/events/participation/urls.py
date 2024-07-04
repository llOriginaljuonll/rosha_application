from django.urls import path
from apps.events.participation import views
app_name = "participation"

urlpatterns = [
    path('form/<pk>', views.ParticipationFormView.as_view(), name="form"),
    path('update/<pk>', views.ParticipationUpdateView.as_view(), name="update"),
]
