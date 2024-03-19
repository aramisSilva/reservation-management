from rest_framework import generics
from .models import Hotel, Quarto
from .serializers import QuartoSerializer
from .base.base_views import HotelBaseView
from drf_yasg.utils import swagger_auto_schema


class HotelCreateView(HotelBaseView, generics.CreateAPIView):
    pass

    @swagger_auto_schema(
        tags=["HOTEIS"],
        operation_summary="Cadastra um hotel",
        operation_description="",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class HotelDetailView(HotelBaseView, generics.RetrieveAPIView):
    lookup_field = 'pk'

    @swagger_auto_schema(
        tags=["HOTEIS"],
        operation_summary="Visualizar os detalhes de um hotel",
        operation_description="",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class HotelUpdateView(HotelBaseView, generics.UpdateAPIView):
    lookup_field = 'pk'

    @swagger_auto_schema(
        tags=["HOTEIS"],
        operation_summary="Atualizar os detalhes de um hotel",
        operation_description="",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["HOTEIS"],
        operation_summary="Atualizar parcialmente os detalhes de um hotel",
        operation_description="",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class HotelListView(HotelBaseView, generics.ListAPIView):
    pass

    @swagger_auto_schema(
        tags=["HOTEIS"],
        operation_summary="Listagem de hoteis cadastrados",
        operation_description="",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class QuartoListCreate(generics.ListCreateAPIView):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        hotel_id = self.kwargs.get('hotel_id')
        if hotel_id is not None:
            queryset = queryset.filter(hotel_id=hotel_id)
        return queryset


class QuartoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer
