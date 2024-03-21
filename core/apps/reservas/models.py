from django.db import models
from ..hoteis.models import Quarto
from ..clientes.models import Cliente

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    quarto = models.ForeignKey(Quarto, related_name='reservas', on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    status = models.CharField(max_length=10, default='confirmada')

    def __str__(self):
        return f"Reserva de {self.cliente.username} para o quarto {self.quarto.numero} de {self.data_inicio} até {self.data_termino}"