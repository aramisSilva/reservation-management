from rest_framework import generics
from ..models import Hotel
from ..serializers import HotelSerializer


class HotelBaseView(generics.GenericAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
