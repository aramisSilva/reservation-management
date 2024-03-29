from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .base.base_views import HotelBaseView, QuartoBaseView, BaseCustomPagination
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..clientes.permissions import IsAdminOrStaff, IsEmployeeUser


class HotelCreateView(HotelBaseView, generics.CreateAPIView):
    permission_classes = [IsAdminOrStaff, IsAuthenticated]

    @swagger_auto_schema(
        tags=["hoteis"],
        operation_summary="Cadastra um hotel",
        operation_description="",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class HotelDetailView(HotelBaseView, generics.RetrieveAPIView):
    lookup_field = 'pk'

    @swagger_auto_schema(
        tags=["hoteis"],
        operation_summary="Visualizar os detalhes de um hotel",
        operation_description="",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class HotelUpdateView(HotelBaseView, generics.UpdateAPIView):
    permission_classes = [IsAdminOrStaff, IsEmployeeUser]
    lookup_field = 'pk'

    @swagger_auto_schema(
        tags=["hoteis"],
        operation_summary="Atualizar os detalhes de um hotel",
        operation_description="",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["hoteis"],
        operation_summary="Atualizar parcialmente os detalhes de um hotel",
        operation_description="",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class HotelListView(HotelBaseView, generics.ListAPIView):
    permission_classes = IsEmployeeUser
    pagination_class = BaseCustomPagination

    @swagger_auto_schema(
        tags=["hoteis"],
        operation_summary="Listagem de hoteis cadastrados",
        operation_description="",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class QuartoListView(QuartoBaseView, generics.ListAPIView):
    permission_classes = [IsEmployeeUser]
    pagination_class = BaseCustomPagination

    @swagger_auto_schema(
        tags=["quartos"],
        operation_summary="Listagem de quartos cadastrados",
        operation_description="",
        manual_parameters=[
            openapi.Parameter(
                'hotel_id', openapi.IN_QUERY, description="ID do hotel para filtrar quartos",
                type=openapi.TYPE_INTEGER
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        hotel_id = self.request.query_params.get('hotel_id')
        if hotel_id is not None:
            queryset = queryset.filter(hotel_id=hotel_id)
        return queryset


class QuartoUpdateView(QuartoBaseView, generics.UpdateAPIView):
    permission_classes = [IsAdminOrStaff, IsEmployeeUser]
    lookup_field = 'pk'

    @swagger_auto_schema(
        tags=["quartos"],
        operation_summary="Atualizar os detalhes de um quarto de hotel",
        operation_description="",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["quartos"],
        operation_summary="Atualizar parcialmente os detalhes de um quarto de hotel",
        operation_description="",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
