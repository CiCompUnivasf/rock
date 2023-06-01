from uuid import uuid4
import json

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rocksite.models import Localizacao, Horizonte, PontoDeAmostragem
from django.forms.models import model_to_dict
from django.db.models import Q


def index(request):
    print('Criando uma localização')
    local = Localizacao(
        descricao="Terreno próximo a casa de seu bida",
        uf="PE",
        municipio="Salgueiro"
    )
    local.save()
    context = {}
    return render(request, "rocksite/index.html", context)

def index(request):
    print('criando um ponto de amostragem')
    local = Localizacao(
        descricao="Terreno próximo a casa de seu bida",
        uf="PE",
        municipio="Salgueiro"
    )
    local.save()
    ponto_de_amostragem = PontoDeAmostragem(
        tipo="perfil completo",
        localizacao = local,
        situacao_coleta="trincheira"
    )
    ponto_de_amostragem.save()
    return HttpResponse("foi salvo o ponto de amostragem")

@csrf_exempt  
def search(request):
    query = None
    parametros = json.loads(request.body)
    parametros_aceitos= ['h2o','calcio','kcl']
    for parametro in parametros_aceitos:
        if parametro in parametros:
            if query is None:
                query = Q(**{parametro:parametros[parametro]})
            else:
                query |= Q(**{parametro:parametros[parametro]})
    print("criando horizonte")
    print(query)
    print(parametros)
    all_horizontes = Horizonte.objects.all().filter(query)
    all_pontos =[] 
    for h in all_horizontes:
        all_pontos.append(h.ponto_de_amostragem)
    localizacaojson = [
        {**model_to_dict(ponto.localizacao),'uso_atual': ponto.uso_atual}
        for ponto in all_pontos]
    return JsonResponse(localizacaojson, safe = False)


    
