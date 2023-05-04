from uuid import uuid4

from django.shortcuts import render
from django.http import HttpResponse
from rocksite.models import Localizacao


def index(request):
    print('Criando um ponto de amostragem')
    local = Localizacao(
        descricao="Terreno próximo a casa de seu bida",
        uf="PE",
        municipio="Salgueiro"
    )
    local.save()
    context = {}
    return render(request, "rocksite/index.html", context)

