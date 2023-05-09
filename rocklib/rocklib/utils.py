
import re
from datetime import datetime


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
