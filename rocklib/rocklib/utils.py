
import re
from datetime import datetime

from bs4 import BeautifulSoup


DATA_RE = re.compile(r'\d{2}/\d{2}/\d{4}')
PATH_BASE = '/home/raul/Downloads/Telegram Desktop/Embrapa/'

def resolve_path(path):
    if 'http' in path:
        return path
    else: return PATH_BASE + path

def get_soup(path):
    with open(resolve_path(path), 'rt', encoding='latin-1') as pathfile:
        text = pathfile.read()
    return BeautifulSoup(text, 'html.parser')

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

def parse_conteudo_propriedades_quimicas(linha_html, nome_html):
    """Este método fará parser de conteúdo de cada linha da tabela de propriedades quimícas 

    Args:
        linha_html (str): O html referente a linha que se quer fazer parser 
        nome_html (str): O nome utilizado para o conteúdo daquela linha

    Returns:
        str: conteúdo
    """
    match = re.match(
        f'\s*<b>\s*{nome_html}\s*</b>\s*:\s+((?:\S+\s*)+)\s+',
        linha_html)
    if match:
        conteudo = match.group(1)
        return conteudo.strip()
    else:
        raise Exception('Estrutura errada')

def get_lista_de_paths(soup: BeautifulSoup):
    lista_fieldset = soup.find('fieldset')
    links = lista_fieldset.find_all('a')
    pares = map(
        lambda link_tag: (link_tag.get_text().strip(), link_tag['href']),
        links
    )
    return pares
