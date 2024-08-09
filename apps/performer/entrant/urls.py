from django.urls import path
from .views import EntrantFormView, EntrantListView, EntrantDetailView, EntrantDeleteView

app_name="entrant"

urlpatterns = [
    path('form/<pk>', EntrantFormView.as_view(), name="form"),
    path('<str:pk>', EntrantListView.as_view(), name="list"),
    path('detail/<pk>/', EntrantDetailView.as_view(), name="detail"),
    path('delete/<pk>/', EntrantDeleteView.as_view(), name="delete"),
]
