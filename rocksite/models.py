from uuid import uuid4

from django.db import models


class PontoDeAmostragem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    numero_pa = models.CharField(max_length=50, null=True)
    data_coleta =  models.DateField(null=True)
    tipo = models.CharField(max_length=100)
    situacao_coleta = models.CharField(max_length=100, null=True)
    material_origem = models.CharField(max_length=100, null=True)
    # TODO: tornar localizacao_id uma chave estrangueira
    localizacao_id = models.UUIDField()

