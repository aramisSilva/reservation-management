from django.urls import path
from .views import (ReservaCreateView, ReservaListView, ReservaDetailView,
                    ReservaUpdateView, ReservaDeleteView)

urlpatterns = [
    path('criar/', ReservaCreateView.as_view(), name='reserva-create'),
    path('<int:pk>/', ReservaDetailView.as_view(), name='reserva-detail'),
    path('listar/', ReservaListView.as_view(), name='reserva-list'),
    path('<int:pk>/atualizar/', ReservaUpdateView.as_view(), name='reserva-update'),
    path('<int:pk>/deletar/', ReservaDeleteView.as_view(), name='reserva-delete'),
]
