from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.HotelCreateView.as_view(), name='hotel-create'),
    path('<int:pk>/', views.HotelDetailView.as_view(), name='hotel-detail'),
    path('list/', views.HotelListView.as_view(), name='hotel-list'),
    path('update/<int:pk>', views.HotelUpdateView.as_view(), name='hotel-update'),
]

