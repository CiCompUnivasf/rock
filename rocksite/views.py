from uuid import uuid4

from django.shortcuts import render
from django.http import HttpResponse
from rocksite.models import Localizacao, Horizonte
from django.forms.models import model_to_dict



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

    
def search(request):
    print("criando horizonte")
    all_horizontes = Horizonte.objects.all()
    horizontesjson = []
    for h in iter(all_horizontes):
        horizontesjson.append(model_to_dict(h))
    return HttpResponse(str(horizontesjson))
