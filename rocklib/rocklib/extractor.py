
from rocklib.logger import logger
from rocklib.utils import get_soup, get_lista_de_paths
from rocklib.pontos_amostragem_extractor import get_identificacao, get_localizacao, get_path_localizacao, get_path_horizontes
from rocklib.horizontes_extractor import get_all_dados_horizonte


def get_all_dados_ponto_amostragem(numero_ponto, path):
    soup = get_soup(path)
    identificacao = get_identificacao(soup)
    localizacao_path = get_path_localizacao(soup)
    localizacao_soup = get_soup(localizacao_path)
    localizacao = get_localizacao(localizacao_soup)
    lista_horizontes_path = get_path_horizontes(soup)
    lista_horizontes_soup = get_soup(lista_horizontes_path)
    lista_horizontes = get_lista_de_paths(lista_horizontes_soup)
    horizontes = []
    for simbolo, horizonte_path in lista_horizontes:
        try:
            horizonte = get_all_dados_horizonte(simbolo, horizonte_path)
            horizontes.append(horizonte)
        except Exception as e:
            logger.debug(f'Exceção ao obter o horizonte {simbolo} para o ponto {numero_ponto}. Exceção: {e}')
    return {
        'numero_pa': numero_ponto,
        'horizontes': horizontes,
        **identificacao,
        **localizacao
    }

def executa_extracao():
    lista_de_pontos_path = '1658783180lpa4171b816865caa59036ee4aa20fffc00b3ee1.html'
    soup = get_soup(lista_de_pontos_path)
    lista_de_paths = list(get_lista_de_paths(soup))
    slice = lista_de_paths[:10]
    logger.debug(len(slice))
    dados = []
    for numero, path in slice:
        try:
            ponto_amostragem = get_all_dados_ponto_amostragem(numero, path)
            dados.append(ponto_amostragem)
        except Exception as e:
            logger.error(f'Erro em ponto {numero}, gerado: {e}')
    return dados
