from django.db import models

# Create your models here.
class Partida(models.Model):
    tipo = models.CharField(max_length=20)
    op1 = models.IntegerField(null=True, blank=True)
    op2 = models.IntegerField(null=True, blank=True)
    acertos = models.IntegerField(default=0)
    totais = models.IntegerField(default=0)
