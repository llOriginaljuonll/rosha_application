from django.urls import path
from apps.events.participation import views

app_name = "participation"

urlpatterns = [
    path('form/', views.ParticipationCreateView.as_view(), name="form"),
    path('update/<int:pk>/', views.ParticipationUpdateView.as_view(), name="update"),
    path('list/', views.ParticipationListView.as_view(), name="list"),
    path('delete/<int:pk>/', views.ParticipationDeleteView.as_view(), name="delete"),
]
