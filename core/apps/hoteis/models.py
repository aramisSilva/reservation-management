from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .choices import CLASSIFICACAO


class Hotel(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    descricao = models.TextField()
    estrelas = models.IntegerField(choices=CLASSIFICACAO, default=3)
    quartos_disponiveis = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000)
        ]
    )

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new:
            quartos_para_criar = [
                Quarto(
                    hotel=self,
                    numero=str(num),
                    tipo='Básico',
                    quantidade_de_camas=2,
                    preco=150.00
                )
                for num in range(1, self.quartos_disponiveis + 1)
            ]
            Quarto.objects.bulk_create(quartos_para_criar)

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
