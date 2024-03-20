from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.HotelCreateView.as_view(), name='hotel-create'),
    path('<int:pk>/', views.HotelDetailView.as_view(), name='hotel-detail'),
    path('list/', views.HotelListView.as_view(), name='hotel-list'),
    path('update/<int:pk>', views.HotelUpdateView.as_view(), name='hotel-update'),
    # url dos quartos
    path('quartos/', views.QuartoListView.as_view(), name='quarto-list'),
    path('quartos/<int:pk>/', views.QuartoUpdateView.as_view(), name='quarto-update'),
]
