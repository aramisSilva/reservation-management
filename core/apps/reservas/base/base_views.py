from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from ..models import Reserva
from ..serializers import ReservaSerializer


class ReservaBaseView(generics.GenericAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class BaseCustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100