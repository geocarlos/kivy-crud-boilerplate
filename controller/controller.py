"""
    The code in this file connects the model and the view.
"""

from model.model import Item, Category, ItemObj, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def add_item(data):
    item = Item(name=data['name'], cat_id=data['cat_id'])
    session.add(item)
    session.commit()


def add_category(data):
    category = Category(name=data['name'])
    session.add(category)
    session.commit()


def get_items():
    items = session.query(Item).all()
    cats = session.query(Category).all()
    return [
        ItemObj(item, next(c for c in cats if c.id == item.cat_id))
        for item in items
    ]


def get_categories():
    return session.query(Category).all()
