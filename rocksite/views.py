from uuid import uuid4

from django.shortcuts import render
from django.http import HttpResponse
from rocksite.models import PontoDeAmostragem


def index(request):
    print('Criando um ponto de amostragem')
    ponto = PontoDeAmostragem(
        tipo="TESTE",
        localizacao_id=uuid4()
    )
    ponto.save()
    context = {}
    return render(request, "rocksite/index.html", context)

