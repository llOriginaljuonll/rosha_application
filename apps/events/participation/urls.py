from django.urls import path
app_name = "participation"

urlpatterns = [
    path('form/<pk>', views.ParticipationFormView.as_view(), name="form"),
]
