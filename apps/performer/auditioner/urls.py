from django.urls import path
from apps.performer.auditioner import views

app_name = 'auditioner'

urlpatterns = [
    path('list', views.AllAuditionerLisview.as_view(), name='all-list'),
    path('<str:pk>', views.AuditionerListView.as_view(), name='list'),
    path('detail/<int:pk>', views.AuditionerDetailView.as_view(), name='detail'),
    path('form/<pk>', views.AuditionerFormView.as_view(), name='form'),
    path('update/<pk>', views.AuditionerUpdateView.as_view(), name='update'),
    path('delete/<pk>', views.AuditionerDeleteView.as_view(), name="delete"),
    # path('items/add-related-item/<int:item_id>/', views.AddRelatedItemView.as_view(), name='add_related_item'),
]
