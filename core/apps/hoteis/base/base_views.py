from rest_framework import generics
from ..models import Hotel, Quarto
from ..serializers import HotelSerializer, QuartoSerializer
from rest_framework.pagination import PageNumberPagination

class HotelBaseView(generics.GenericAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class QuartoBaseView(generics.GenericAPIView):
    queryset = Quarto.objects.all()
    serializer_class = QuartoSerializer

class BaseCustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100