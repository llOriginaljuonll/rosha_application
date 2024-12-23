from django.urls import path
from apps.performer.auditioner import views

app_name = 'auditioner'

urlpatterns = [
    path('list', views.AllAuditionerListview.as_view(), name='all-list'),
    path('<str:pk>', views.AuditionerListView.as_view(), name='list'),
    path('detail/<int:pk>', views.AuditionerDetailView.as_view(), name='detail'),
    path('<int:audition_id>/form/', views.AuditionerCreateView.as_view(), name='form'),
    path('update/<int:pk>', views.AuditionerUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.AuditionerDeleteView.as_view(), name="delete"),
]
