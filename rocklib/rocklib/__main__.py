
from bs4 import BeautifulSoup

from rocklib.pontos_amostragem_extractor import get_identificacao

with open('exemplo.html', 'rt', encoding='latin-1') as exemplofile:
    exemplotext = exemplofile.read()


soup = BeautifulSoup(exemplotext, 'html.parser')

print(get_identificacao(soup))