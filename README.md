# rock

# Como rodar local

Antes de tudo, realize o clone do projeto em sua maquina local, e mova-se para dentro do diretório do projeto. Faça instalação do python, se necessário.

Após isso, instale as dependências:

```sh
pip install -r requirements.txt
```

Com isso você pode subir o servidor localmente, ou utilizar a biblioteca `rocklib`, separadamente, veja como:

```sh
# subir servidor
python manage.py runserver

# Executa o script `rocklib/__main__.py` da biblioteca rocklib.
# No futuro este script irá fazer a raspagem de dados
cd rocklib
python -m rocklib
```

## Criar tabelas

Após criar um model no arquivo `rocksite/models.py` você deve criar uma migration e executa-la, dessa forma:

```sh
python manage.py makemigrations
python manage.py migrate
```
