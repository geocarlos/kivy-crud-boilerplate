"""
    The code in this file connects the model and the view.
"""

from model.model import Item, Category, ItemObj
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ----------------------------------------------------------------------

"""
    Connect to our SQLite database and return a Session object
"""
engine = create_engine("sqlite:///model/db/app.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# ----------------------------------------------------------------------

"""
    Add a new item to the Item table. Data must be in a dictionary.
"""
def add_item(data):
    item = Item()
    item.name = data['name']
    item.cat_id = data['cat_id']
    session.add(item)
    session.commit()
    session.close()

"""
    Add a new category to the Category table. Data must be in a dictionary.
"""
def add_category(data):
    category = Category()
    category.name = data['name']
    session.add(category)
    session.commit()
    session.close()

"""
    Get everything from tables Item and Category and create a list of ItemObj
"""
def get_items():
    items = session.query(Item).all()
    cats = session.query(Category).all()
    itemObjs = []
    for item in items:
        cat = [c for c in cats if c.id == item.cat_id][0]
        itemObj = ItemObj(item, cat)
        itemObjs.append(itemObj)
    session.close()
    return itemObjs

def get_categories():
    categories = session.query(Category).all()
    session.close()
    return categories
