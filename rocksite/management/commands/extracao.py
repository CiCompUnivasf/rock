
import logging

from django.core.management.base import BaseCommand
import rocklib

from rocksite.models import Localizacao, Horizonte, PontoDeAmostragem

class Command(BaseCommand):
    help = 'Comando para extração e persistência dos dados da Embrapa'

    def configure_verbosity(self, verbosity):
        levels = {
            0: logging.ERROR,
            1: logging.INFO,
            2: logging.DEBUG,
            3: logging.DEBUG,
        }
        level = levels[verbosity]
        rocklib.logger.logger.setLevel(level)

    def handle(self, *args, **options):
        self.configure_verbosity(options['verbosity'])
        dados = rocklib.executa_extracao()
        for ponto in dados:
            local = Localizacao(
                uf=ponto['uf'],
                municipio=ponto['municipio'],
                descricao=ponto['descricao'])
            local.save()
            ponto_model = PontoDeAmostragem(
                numero_pa=ponto['numero_pa'],
                data_coleta=ponto['data_coleta'],
                tipo=ponto['tipo'],
                situacao_coleta=ponto['situacao_coleta'],
                material_origem=ponto['material_origem'],
                localizacao=local,
                uso_atual=ponto['uso_atual'])
            ponto_model.save()
            for horizonte in ponto['horizontes']:
                horizonte_model = Horizonte( profundidade_superior = horizonte['profundidade_superior'], profundidade_inferior = horizonte['profundidade_inferior'], h2o = horizonte['h2o'],kcl = horizonte['kcl'], calcio = horizonte['calcio'], simbolo = horizonte['simbolo'],ponto_de_amostragem = ponto_model)
                horizonte_model.save()
       
        self.stdout.write(self.style.SUCCESS('salvo com sucesso!!'))
