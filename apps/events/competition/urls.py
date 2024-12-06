from django.urls import path
from apps.events.competition.views import ComptFormView, ComptListView, ComptUpdateView, ComptDeleteView

app_name="compt"

urlpatterns = [
    path('form/', ComptFormView.as_view(), name='form'),
    path('competition_list/', ComptListView.as_view(), name='competition_list'),
    path('update/<pk>', ComptUpdateView.as_view(), name='update'),
    path('delete/<pk>', ComptDeleteView.as_view(), name='delete'),
]
