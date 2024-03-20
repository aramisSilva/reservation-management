from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.HotelCreateView.as_view(), name='hotel-create'),
    path('<int:pk>/', views.HotelDetailView.as_view(), name='hotel-detail'),
    path('lista/', views.HotelListView.as_view(), name='hotel-list'),
    path('<int:pk>/atualizar/', views.HotelUpdateView.as_view(), name='hotel-update'),
    # url dos quartos
    path('quartos/lista/', views.QuartoListView.as_view(), name='quarto-list'),
    path('quartos/<int:pk>/atualizar/', views.QuartoUpdateView.as_view(), name='quarto-update'),
]
