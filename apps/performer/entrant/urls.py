from django.urls import path
from .views import EntrantFormView

app_name="entrant"

urlpatterns = [
    path('form/<pk>', EntrantFormView.as_view(), name="form"),
]
