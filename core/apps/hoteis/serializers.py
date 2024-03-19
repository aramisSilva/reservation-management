from rest_framework import serializers
from .models import Hotel, Quarto


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['nome', 'endereco', 'descricao', 'estrelas', 'quartos_disponiveis']


class QuartoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quarto
        fields = ['hotel', 'numero', 'tipo', 'quantidade_de_camas', 'preco']
