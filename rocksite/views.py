from uuid import uuid4

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rocksite.models import Localizacao, Horizonte, PontoDeAmostragem
from django.forms.models import model_to_dict



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
    print("criando horizonte")
    all_horizontes = Horizonte.objects.all().filter(h2o__gte=0)
    horizontesjson = []
    for h in iter(all_horizontes):
        horizontesjson.append(model_to_dict(h))
    return JsonResponse(horizontesjson, safe = False)


    
