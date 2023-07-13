# rock

# Como rodar local

Antes de tudo, realize o clone do projeto em sua maquina local, e mova-se para dentro do diretório do projeto. Faça instalação do python, se necessário.

Após isso, instale as dependências:

```sh
pip install -r requirements.txt
```

Para criar as tabelas no banco de dados, e popula-lo, execute:

```sh
# Cria tabelas
python manage.py migrate
# Executa a extração
python manage.py extracao
```

É importante notar que é necessário ter os arquivos da embrapa em seu computador para executar a extração. Após te-los, é necessário adicionar o caminho dos arquivos na variável `PATH_BASE` do arquivo `rocklib/rocklib/utils.py`.

Com isso você pode subir o servidor localmente, veja como:

```sh
# subir servidor
python manage.py runserver
```

## Criar tabelas

Após criar um model no arquivo `rocksite/models.py` você deve criar uma migration e executa-la, dessa forma:

```sh
python manage.py makemigrations
python manage.py migrate
```
