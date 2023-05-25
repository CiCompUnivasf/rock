
import re

from bs4 import BeautifulSoup

from rocklib.logger import logger
from rocklib.utils import (
    parse_conteudo,
    parse_conteudo_propriedades_quimicas,
    get_soup)


CALCIO_RE = re.compile(r'\d+\.\d+')

def map_optional(func, value):
    """If value is None return it, otherwise call func with value"""
    if value is None:
        return None
    else: return func(value)

def get_identificacao(soup: BeautifulSoup):
    superior = None
    inferior = None
    identificacao_index = -1
    fieldset = soup.find_all('fieldset')
    identificacao_fieldset = fieldset[identificacao_index]
    raw_html = str(identificacao_fieldset)
    lines = raw_html.split('<b>')
    try:
        superior = int(parse_conteudo(lines, 'Profundidade Superior'))
        inferior = int(parse_conteudo(lines, 'Profundidade Inferior'))
    except Exception as e:
        logger.debug(f"Erro ao obter profundidade do horizonte. Erro: {str(e)}.")
    return {
        'profundidade_superior': superior,
        'profundidade_inferior': inferior
    }

def get_propriedades_quimicas(soup: BeautifulSoup):
    h2o = None
    kcl = None
    calcio_number = None
    propriedades_index = -1
    fieldset = soup.find_all('fieldset')
    identificacao_fieldset = fieldset[propriedades_index]
    raw_html = str(identificacao_fieldset)
    lines = raw_html.split('<br/>')
    try:
        h2o = map_optional(float, parse_conteudo_propriedades_quimicas(lines, 'H<sub>2</sub>O'))
        kcl = map_optional(float, parse_conteudo_propriedades_quimicas(lines, 'KCl'))
        calcio = parse_conteudo_propriedades_quimicas(lines, 'Cálcio')
        if calcio:
            calcio_match = re.search(CALCIO_RE, calcio)
            if calcio_match:
                calcio_number = float(calcio_match.group(0))
    except Exception as e:
        logger.debug(f'Erro ao obter propriedades químicas: {e}')
    return {
        'h2o': h2o,
        'kcl': kcl,
        'calcio': calcio_number
    }

def get_path_propriedades_quimicas(soup: BeautifulSoup):
    links_index = 1
    propriedades_index = 2
    fieldset = soup.find_all('fieldset')
    links_fieldset = fieldset[links_index]
    links = links_fieldset.find_all('a')
    link_tag = links[propriedades_index]
    return link_tag['href']

def get_all_dados_horizonte(horizonte_simbolo, path):
    soup = get_soup(path)
    identificacao = get_identificacao(soup)
    propriedades_path = get_path_propriedades_quimicas(soup)
    propriedades_soup = get_soup(propriedades_path)
    propriedades = get_propriedades_quimicas(propriedades_soup)
    return {
        'simbolo': horizonte_simbolo,
        **identificacao,
        **propriedades
    }
