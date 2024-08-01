from django.urls import path
from .views import EntrantFormView, EntrantListView

app_name="entrant"

urlpatterns = [
    path('form/<pk>', EntrantFormView.as_view(), name="form"),
    path('<str:pk>', EntrantListView.as_view(), name="list"),
]
