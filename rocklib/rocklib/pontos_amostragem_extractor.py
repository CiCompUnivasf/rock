
from bs4 import BeautifulSoup

from rocklib.utils import parse_data, parse_conteudo


def get_identificacao(soup: BeautifulSoup):
    indentificacao_index = -1
    fieldset = soup.find_all('fieldset')
    identificacao_fieldset = fieldset[indentificacao_index]
    raw_html = str(identificacao_fieldset)
    lines = raw_html.split('<b>')
    data = parse_data(lines)
    tipo = parse_conteudo(lines, 'Tipo')
    situacao_coleta = parse_conteudo(lines, 'Situação coleta das amostras')
    material_origem = parse_conteudo(lines, 'Material de Origem')
    uso_atual = parse_conteudo(lines, 'Uso Atual')
    return {
        'data_coleta': data,
        'tipo': tipo,
        'situacao_coleta': situacao_coleta,
        'material_origem': material_origem,
        'uso_atual': uso_atual,
    }

def get_localizacao(soup: BeautifulSoup):
    localizacao_index = -1
    fieldset = soup.find_all('fieldset')
    localizacao_fieldset = fieldset[localizacao_index]
    raw_html = str(localizacao_fieldset)
    lines = raw_html.split('<b>')
    descricao = parse_conteudo(lines, 'Localização descritiva')
    uf = parse_conteudo(lines, 'UF')
    municipio = parse_conteudo(lines, 'Município')
    return {
        'descricao': descricao,
        'uf': uf,
        'municipio': municipio
    }

def get_path_localizacao(soup: BeautifulSoup):
    links_index = 1
    fieldset = soup.find_all('fieldset')
    links_fieldset = fieldset[links_index]
    link_tag = links_fieldset.find('a')
    return link_tag['href']

def get_path_horizontes(soup: BeautifulSoup):
    relacionados_index = 0
    horizontes_link_index = 1
    fieldset = soup.find_all('fieldset')
    relacionados_fiedset = fieldset[relacionados_index]
    links = relacionados_fiedset.find_all('a')
    link_tag = links[horizontes_link_index]
    return link_tag['href']
