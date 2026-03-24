from django.db import models

from core.models.acessorio import Acessorio
from core.models.cor import Cor
from core.models.modelo import Modelo


class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name='veiculos', null=True, blank=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name='veiculos', null=True, blank=True)
    acessorios = models.ManyToManyField(Acessorio, related_name='veiculos')

    def __str__(self):
        return f'({self.ano} {self.preco})'
