from django.db import models
# from core.apps.clientes.models import Cliente
from core.apps.hoteis.models import Quarto


class Reserva(models.Model):
    # cliente = models.ForeignKey(Cliente, related_name='reservas', on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, related_name='reservas', on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    status = models.CharField(max_length=50)
