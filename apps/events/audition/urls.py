from django.urls import path
from apps.events.audition import views

app_name = 'audition'

urlpatterns = [
    path('', views.AuditionListView.as_view(),name='list'),
    path('competition_form/', views.AuditionCreateView.as_view(), name='form'),
    path('competition_update/<pk>', views.AuditionUpdateView.as_view(), name="update"),
    path('competition_delete/<pk>', views.AuditionDeleteView.as_view(), name="delete"),
]