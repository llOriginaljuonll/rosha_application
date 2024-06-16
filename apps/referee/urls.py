from django.urls import path
from apps.referee import views

app_name = "referee"

urlpatterns = [
    path('referee_form/<pk>', views.ScoreFormView.as_view(), name="form"),
]
