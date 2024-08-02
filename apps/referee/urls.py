from django.urls import path
from apps.referee import views

app_name = "referee"

urlpatterns = [
    path('update/<pk>', views.ScoreUpdateView.as_view(), name="update"),
    path('entrant_score/<pk>', views.EntrantScoreView.as_view(), name="entrant-score"),
]
