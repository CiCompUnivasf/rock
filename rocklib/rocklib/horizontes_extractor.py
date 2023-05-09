
import re

from bs4 import BeautifulSoup

from rocklib.utils import parse_data, parse_conteudo, parse_conteudo_propriedades_quimicas


CALCIO_RE = re.compile(r'\d+\.\d+')

def get_identificacao(soup: BeautifulSoup):
    identificacao_index = -1
    superior_index = 1
    inferior_index = 2
    fieldset = soup.find_all('fieldset')
    identificacao_fieldset = fieldset[identificacao_index]
    raw_html = str(identificacao_fieldset)
    lines = raw_html.split('<b>')
    superior = parse_conteudo(lines[superior_index], 'Profundidade Superior')
    inferior = parse_conteudo(lines[inferior_index], 'Profundidade Inferior')
    return {
        'profundidade_superior': int(superior),
        'profundidade_inferior': int(inferior)
    }

def get_propriedades_quimicas(soup: BeautifulSoup):
    propriedades_index = -1
    h2o_index = 4
    kcl_index = 6
    calcio_index = 12
    fieldset = soup.find_all('fieldset')
    identificacao_fieldset = fieldset[propriedades_index]
    raw_html = str(identificacao_fieldset)
    lines = raw_html.split('<br/>')
    h2o = parse_conteudo_propriedades_quimicas(lines[h2o_index], 'H<sub>2</sub>O')
    kcl = parse_conteudo_propriedades_quimicas(lines[kcl_index], 'KCl')
    calcio = parse_conteudo_propriedades_quimicas(lines[calcio_index], 'Cálcio')
    calcio_match = re.search(CALCIO_RE, calcio)
    if calcio_match:
        calcio_number = float(calcio_match.group(0))
    else:
        calcio_number = None
    return {
        'h2o': float(h2o),
        'kcl': float(kcl),
        'calcio': calcio_number
    }
