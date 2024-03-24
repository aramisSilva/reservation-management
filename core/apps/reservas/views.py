from django.core.exceptions import ValidationError
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .base.base_views import ReservaBaseView, BaseCustomPagination
from .models import Reserva
from .tasks import enviar_email_reserva
from django.shortcuts import get_object_or_404

from ..clientes.models import Cliente


class ReservaCreateView(ReservaBaseView, generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        cliente = get_object_or_404(Cliente, pk=user.pk)
        quarto_id = serializer.validated_data.get('quarto').id
        data_inicio = serializer.validated_data.get('data_inicio')
        data_termino = serializer.validated_data.get('data_termino')

        reservas_existentes = Reserva.objects.filter(
            quarto=quarto_id,
            data_termino__gte=data_inicio,
            data_inicio__lte=data_termino,
            status='confirmada'
        ).exists()

        if reservas_existentes:
            raise ValidationError('Este quarto não está disponível para as datas selecionadas.')

        reserva = serializer.save(cliente=cliente)

        mensagem_email = f"Parabéns {reserva.cliente.username}, sua reserva foi confirmada para o quarto {reserva.quarto.numero} do hotel {reserva.quarto.hotel.nome}. Você ficará hospedado de {reserva.data_inicio} até {reserva.data_termino}."

        enviar_email_reserva.delay(
            email_destinatario=reserva.cliente.email,
            mensagem=mensagem_email
        )


class ReservaDetailView(ReservaBaseView, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'


class ReservaUpdateView(ReservaBaseView, generics.UpdateAPIView):
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def patch(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ReservaDeleteView(ReservaBaseView, generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.status = 'cancelada'
        instance.save()


class ReservaListView(ReservaBaseView, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = BaseCustomPagination
