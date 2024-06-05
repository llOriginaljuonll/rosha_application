from django.urls import path
from apps.competition import views

app_name = 'competition'

urlpatterns = [
    path('', views.CompetitionListView.as_view(),name='list'),
    path('competition_form/', views.CompetitionCreateView.as_view(), name='form'),
    path('competition/<pk>', views.CompetitionDetailView.as_view(), name='detail'),
]