
from bs4 import BeautifulSoup

from rocklib.horizontes_extractor import get_identificacao, get_propriedades_quimicas

with open('exemplo-propriedades-quimicas.html', 'rt', encoding='latin-1') as exemplofile:
    exemplotext = exemplofile.read()


soup = BeautifulSoup(exemplotext, 'html.parser')

prop = get_propriedades_quimicas(soup)

print(prop)
