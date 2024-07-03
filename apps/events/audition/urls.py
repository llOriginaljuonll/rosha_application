from django.urls import path
from apps.events.audition import views

app_name = 'audition'

urlpatterns = [
    path('', views.AuditionListView.as_view(),name='list'),
    path('audition_form/', views.AuditionCreateView.as_view(), name='form'),
    path('audition_update/<pk>', views.AuditionUpdateView.as_view(), name="update"),
    path('audition_delete/<pk>', views.AuditionDeleteView.as_view(), name="delete"),
]