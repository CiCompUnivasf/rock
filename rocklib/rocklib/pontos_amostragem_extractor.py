
from bs4 import BeautifulSoup

from rocklib.utils import parse_data, parse_conteudo


def get_identificacao(soup: BeautifulSoup):
    indentificacao_index = -1
    data_index = 1
    tipo_index = 3
    situacao_index = 4
    material_index = 5
    fieldset = soup.find_all('fieldset')
    identificacao_fieldset = fieldset[indentificacao_index]
    raw_html = str(identificacao_fieldset)
    lines = raw_html.split('<b>')
    data = parse_data(lines[data_index])
    tipo = parse_conteudo(lines[tipo_index], 'Tipo')
    situacao_coleta = parse_conteudo(lines[situacao_index], 'Situação coleta das amostras')
    material_origem = parse_conteudo(lines[material_index], 'Material de Origem')
    return {
        'data_coleta': data,
        'tipo': tipo,
        'situacao_coleta': situacao_coleta,
        'material_origem': material_origem
    }

def get_localizacao(soup: BeautifulSoup):
    localizacao_index = -1
    descricao_index = 1
    uf_index = 2
    municipio_index = 3
    fieldset = soup.find_all('fieldset')
    localizacao_fieldset = fieldset[localizacao_index]
    raw_html = str(localizacao_fieldset)
    lines = raw_html.split('<b>')
    descricao = parse_conteudo(lines[descricao_index], 'Localização descritiva')
    uf = parse_conteudo(lines[uf_index], 'UF')
    municipio = parse_conteudo(lines[municipio_index], 'Município')
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
