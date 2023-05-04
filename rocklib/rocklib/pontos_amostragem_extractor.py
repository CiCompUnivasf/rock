
import re
from datetime import datetime

from bs4 import BeautifulSoup


DATA_RE = re.compile(r'\d{2}/\d{2}/\d{4}')

def parse_data(data):
    match = DATA_RE.search(data)
    if match:
        datapart = match.group(0)
        datetime_part = datetime.strptime(datapart, '%d/%m/%Y')
        return datetime_part.date()
    else:
        raise Exception('Estrutura errada')

def parse_conteudo(linha_html, nome_html):
    """Este método fará parser de conteúdo de cada linha da tabela de identificação

    Args:
        linha_html (str): O html referente a linha que se quer fazer parser 
        nome_html (str): O nome utilizado para o conteúdo daquela linha

    Returns:
        str: conteúdo
    """
    match = re.match(
        f'\s*{nome_html}\s*</b>\s*:\s+((?:\S+\s*)+)\s+',
        linha_html)
    if match:
        conteudo = match.group(1)
        return conteudo.strip()
    else:
        raise Exception('Estrutura errada')

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
