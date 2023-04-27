
from bs4 import BeautifulSoup

def get_identificacao(soup: BeautifulSoup):
    fieldset = soup.find_all('fieldset')
    identificacao_fieldset = fieldset[-1]
    lines = list(identificacao_fieldset.strings)
    return lines 
