from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListView.as_view(), name='event_list'),
    path('dodaj/', views.EventCreateView.as_view(), name='event_create'),
    path('wydarzenie/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('edytuj/<int:pk>/', views.EventUpdateView.as_view(), name='event_update'),
    path('wydarzenie/<int:event_pk>/dodaj-goscia/', views.GuestCreateView.as_view(), name='guest_create'),
    path('gosc/<int:pk>/przelacz/', views.toggle_guest_status, name='toggle_guest_status'),
]