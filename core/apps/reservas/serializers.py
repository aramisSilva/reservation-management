from rest_framework import serializers
from .models import Reserva


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'cliente', 'quarto', 'data_inicio', 'data_termino', 'status']
