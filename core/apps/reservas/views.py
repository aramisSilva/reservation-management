from django.core.exceptions import ValidationError
from rest_framework import generics, status
from rest_framework.response import Response
from .base.base_views import ReservaBaseView, BaseCustomPagination
from .models import Reserva


class ReservaCreateView(ReservaBaseView, generics.CreateAPIView):
    def perform_create(self, serializer):
        quarto_id = serializer.validated_data.get('quarto').id
        data_inicio = serializer.validated_data.get('data_inicio')
        data_termino = serializer.validated_data.get('data_termino')

        reservas_existentes = Reserva.objects.filter(
            quarto_id=quarto_id,
            data_termino__gte=data_inicio,
            data_inicio__lte=data_termino
        ).exists()

        if reservas_existentes:
            raise ValidationError('Este quarto não está disponível para as datas selecionadas.')

        serializer.save()


class ReservaDetailView(ReservaBaseView, generics.RetrieveAPIView):
    lookup_field = 'pk'


class ReservaUpdateView(ReservaBaseView, generics.UpdateAPIView):
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def patch(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ReservaDeleteView(ReservaBaseView, generics.DestroyAPIView):
    lookup_field = 'pk'


class ReservaListView(ReservaBaseView, generics.ListAPIView):
    pagination_class = BaseCustomPagination