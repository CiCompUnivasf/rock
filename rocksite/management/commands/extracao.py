from django.core.management.base import BaseCommand
import rocklib
from rocksite.models import Localizacao,Horizonte, PontoDeAmostragem

class Command(BaseCommand):
    help = 'Descrição do meu comando'

    def handle(self, *args, **options):
        dados = rocklib.executa_extracao()
        for ponto in dados:
            local = Localizacao(uf = ponto['uf'],municipio = ponto['municipio'],descricao = ponto['descricao'])
            local.save()
            ponto_model = PontoDeAmostragem( numero_pa = ponto['numero_pa'], data_coleta = ponto['data_coleta'], tipo = ponto['tipo'],  situacao_coleta = ponto['situacao_coleta'],  material_origem = ponto['material_origem'], localizacao = local)
            ponto_model.save()
            for horizonte in ponto['horizontes']:
                horizonte_model = Horizonte( profundidade_superior = horizonte['profundidade_superior'], profundidade_inferior = horizonte['profundidade_inferior'], h2o = horizonte['h2o'],kci = horizonte['kcl'], calcio = horizonte['calcio'], simbolo = horizonte['simbolo'],ponto_de_amostragem = ponto_model)
       
        self.stdout.write('salvo com sucesso!!')