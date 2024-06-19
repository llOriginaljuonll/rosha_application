from django.urls import path
from apps.competition import views

app_name = 'competition'

urlpatterns = [
    path('', views.CompetitionListView.as_view(),name='list'),
    path('competition_form/', views.CompetitionCreateView.as_view(), name='form'),
    path('competition_update/<pk>', views.CompetitionUpdateView.as_view(), name="update"),
    path('competition_delete/<pk>', views.CompetitionDeleteView.as_view(), name="delete"),
]