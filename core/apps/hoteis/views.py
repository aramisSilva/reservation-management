# hoteis/views.py
from rest_framework import generics
from .models import Hotel, Quarto
from .serializers import HotelSerializer, QuartoSerializer


class HotelListCreate(generics.CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelDetail(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    lookup_field = 'pk'


class HotelUpdateView(generics.UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    lookup_field = 'pk'


class QuartoListCreate(generics.ListCreateAPIView):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer

    def get_queryset(self):
        """
        Opcionalmente restrinja a lista de quartos a um hotel específico,
        passando um 'hotel_id' na URL.
        """
        queryset = super().get_queryset()
        hotel_id = self.kwargs.get('hotel_id')
        if hotel_id is not None:
            queryset = queryset.filter(hotel_id=hotel_id)
        return queryset


class QuartoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer
