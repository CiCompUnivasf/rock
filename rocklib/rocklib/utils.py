
import re
from datetime import datetime

from bs4 import BeautifulSoup

from rocklib.logger import logger


DATA_RE = re.compile(r'\d{2}/\d{2}/\d{4}')
PATH_BASE = 'C:\\Users\\jpaul\\Desktop\\var\\www\\solos\\html\\16587831804171ba22bccc0b7f83270e419def938bf4de9\\'

def resolve_path(path):
    if 'http' in path:
        return path
    else: return PATH_BASE + path

def map_optional(func, value):
    """If value is None return it, otherwise call func with value"""
    if value is None:
        return None
    else: return func(value)

def get_soup(path):
    with open(resolve_path(path), 'rt', encoding='latin-1') as pathfile:
        text = pathfile.read()
    return BeautifulSoup(text, 'html.parser')

def parse_data(linhas_html):
    data = parse_conteudo(linhas_html, 'Data da Coleta')
    if data:
        match = DATA_RE.search(data)
        if match:
            datapart = match.group(0)
            datetime_part = datetime.strptime(datapart, '%d/%m/%Y')
            return datetime_part.date()
    logger.debug('Não foi posssível realizar parser da data')
    return None

def parse_conteudo(linhas_html, nome_html):
    """Este método fará parser de conteúdo de cada linha da tabela de identificação

    Args:
        linhas_html (list[str]): Lista de html's referente as possiveis linhas que se quer fazer parser 
        nome_html (str): O nome utilizado para o conteúdo daquela linha

    Returns:
        str: conteúdo
    """
    found = False
    for linha_html in linhas_html:
        if linha_html.strip().startswith(nome_html):
            found = True
            break
    if not found:
        logger.debug(f"Não foi possível obter o dado {nome_html}")
        return None
    match = re.match(
        f'\s*{nome_html}\s*</b>\s*:\s+((?:\S+\s*)+)\s+',
        linha_html)
    if match:
        conteudo = match.group(1)
        return conteudo.strip()
    else:
        logger.debug(f'Não foi possível realizar parser da linha com nome "{nome_html}"')
        return None

def parse_conteudo_propriedades_quimicas(linhas_html, nome_html):
    """Este método fará parser de conteúdo de cada linha da tabela de propriedades quimícas 

    Args:
        linhas_html (list[str]): Lista de html's referente as possiveis linhas que se quer fazer parser 
        nome_html (str): O nome utilizado para o conteúdo daquela linha

    Returns:
        str: conteúdo
    """
    for linha_html in linhas_html:
        match = re.match(
            f'\s*<b>\s*{nome_html}\s*</b>\s*:\s+((?:\S+\s*)+)\s+',
            linha_html)
        if match:
            conteudo = match.group(1)
            return conteudo.strip()
    logger.debug(f"Não foi possível obter o dado {nome_html}")
    return None

def get_lista_de_paths(soup: BeautifulSoup):
    lista_fieldset = soup.find('fieldset')
    links = lista_fieldset.find_all('a')
    pares = map(
        lambda link_tag: (link_tag.get_text().strip(), link_tag['href']),
        links
    )
    return pares
