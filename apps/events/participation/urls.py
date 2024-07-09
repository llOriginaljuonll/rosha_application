from django.urls import path
from apps.events.participation import views

app_name = "participation"

urlpatterns = [
    path('form/<pk>', views.ParticipationFormView.as_view(), name="form"),
    path('update/<pk>', views.ParticipationUpdateView.as_view(), name="update"),
    path('list/', views.ParticipationListView.as_view(), name="list"),
    path('participation_delete/<pk>', views.ParticipationDeleteView.as_view(), name="delete"),
]
