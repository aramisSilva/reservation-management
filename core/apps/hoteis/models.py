from django.db import models


class Hotel(models.Model):

    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    descricao = models.TextField()
    estrelas = models.IntegerField()
    quartos_disponiveis = models.IntegerField()

    def __str__(self):
        return self.nome


class Quarto(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='quartos', on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    quantidade_de_camas = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tipo} - Quarto {self.numero} do {self.hotel.nome}"