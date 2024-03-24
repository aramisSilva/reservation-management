from rest_framework import serializers
from .models import Reserva, Quarto


class ReservaSerializer(serializers.ModelSerializer):
    hotel_id = serializers.IntegerField(write_only=True)
    numero_quarto = serializers.IntegerField(write_only=True)

    class Meta:
        model = Reserva
        fields = ['id',  'hotel_id', 'numero_quarto', 'data_inicio', 'data_termino']
        extra_kwargs = {'cliente': {'read_only': True}}

    def validate(self, attrs):
        hotel_id = attrs.pop('hotel_id')
        numero_quarto = attrs.pop('numero_quarto')
        data_inicio = attrs['data_inicio']
        data_termino = attrs['data_termino']

        try:
            quarto = Quarto.objects.get(numero=numero_quarto, hotel_id=hotel_id)
        except Quarto.DoesNotExist:
            raise serializers.ValidationError("Esse hotel não possui este quarto")

        reservas_existentes = Reserva.objects.filter(
            quarto=quarto,
            data_termino__gte=data_inicio,
            data_inicio__lte=data_termino,
            status='confirmada'
        ).exists()

        if reservas_existentes:
            raise serializers.ValidationError("Este quarto não está disponível para as datas selecionadas.")

        attrs['quarto'] = quarto
        return attrs
