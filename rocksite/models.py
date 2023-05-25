from uuid import uuid4

from django.db import models


class Localizacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    descricao = models.CharField(max_length=500, null=False)
    uf = models.CharField(max_length=2, null=False)
    municipio = models.CharField(max_length=50, null=False)

class PontoDeAmostragem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    numero_pa = models.CharField(max_length=50, null=True)
    data_coleta =  models.DateField(null=True)
    tipo = models.CharField(max_length=100)
    situacao_coleta = models.CharField(max_length=100, null=True)
    material_origem = models.CharField(max_length=100, null=True)
    uso_atual = models.CharField(max_length=100, null=True)
    localizacao =  models.ForeignKey(Localizacao, on_delete=models.CASCADE)

class Horizonte(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    profundidade_superior = models.IntegerField(null=True)
    profundidade_inferior = models.IntegerField(null=True)
    h2o = models.FloatField(null=True)
    kcl = models.FloatField(null=True)
    calcio = models.FloatField(null=True)
    simbolo = models.CharField(max_length=3, null=False)
    ponto_de_amostragem = models.ForeignKey(PontoDeAmostragem, on_delete=models.CASCADE, null=True)
