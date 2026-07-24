# Boilerplate para CRUD com KivyMD

Este projeto tem como objetivo reunir o mínimo de código necessário para iniciar um aplicativo com CRUD usando KivyMD. É usada a abordagem MVC.

## Stack

- **[Kivy](https://kivy.org) 2.3+** - framework de UI multiplataforma
- **[KivyMD](https://kivymd.readthedocs.io) 1.1.1** - componentes Material Design para Kivy
- **[SQLAlchemy](https://www.sqlalchemy.org) 2.0+** - ORM para acesso ao banco de dados
- **SQLite** - banco de dados embutido, fácil de distribuir com aplicativos desktop ou mobile
- **[uv](https://docs.astral.sh/uv/)** - gerenciador moderno de pacotes e projetos Python

## Requisitos

- Python 3.11 ou 3.12
- `uv` ([instruções de instalação](https://docs.astral.sh/uv/getting-started/installation/))

## Instalação e execução

```bash
uv sync
uv run app.py
```

O comando `uv sync` cria o ambiente virtual e instala todas as dependências automaticamente. Não é necessário configurar `pip install` ou `venv` manualmente.

## Estrutura do projeto

```
app.py              # Ponto de entrada
model/
    model.py        # Modelos ORM do SQLAlchemy (Item, Category)
    db/app.db       # Banco de dados SQLite (criado automaticamente na primeira execução)
controller/
    controller.py   # Operações CRUD conectando model e view
view/
    view.py         # Classes do app e das telas
    my.kv           # Definições de layout KivyMD
```
