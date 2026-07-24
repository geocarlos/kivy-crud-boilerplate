# Boilerplate for KivyMD CRUD

This project is intended to put together minimal code necessary to start a [KivyMD](https://kivymd.readthedocs.io) application with CRUD. The MVC approach is used.

## Stack

- **[Kivy](https://kivy.org) 2.3+** - cross-platform UI framework
- **[KivyMD](https://kivymd.readthedocs.io) 1.1.1** - Material Design components for Kivy
- **[SQLAlchemy](https://www.sqlalchemy.org) 2.0+** - ORM for database access
- **SQLite** - embedded database, easy to ship with desktop or mobile apps
- **[uv](https://docs.astral.sh/uv/)** - fast Python package and project manager

## Requirements

- Python 3.11 or 3.12
- `uv` ([install instructions](https://docs.astral.sh/uv/getting-started/installation/))

## Install and run

```bash
uv sync
uv run app.py
```

`uv sync` creates a virtual environment and installs all dependencies automatically. No manual `pip install` or `venv` setup needed.

## Project structure

```
app.py              # Entry point
model/
    model.py        # SQLAlchemy ORM models (Item, Category)
    db/app.db       # SQLite database (auto-created on first run)
controller/
    controller.py   # CRUD operations connecting model and view
view/
    view.py         # App and screen classes
    my.kv           # KivyMD layout definitions
```
