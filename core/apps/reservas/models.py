from django.db import models
from ..hoteis.models import Quarto


class Reserva(models.Model):
    quarto = models.ForeignKey(Quarto, related_name='reservas', on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    status = models.CharField(max_length=50)
