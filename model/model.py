"""
    This is where the app models are created.
"""

from sqlalchemy import Table, Column, create_engine
from sqlalchemy import ForeignKey, String, Unicode
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


engine = create_engine("sqlite:///model/db/app.db", echo=True)
Base = declarative_base(engine)

"""
    Class to turn tables into one Python object
"""


class ItemObj(object):

    def __init__(self, item, category, *args):
        super(EntryObj, self).__init__(*args)
        self.id = entry.id
        self.item = item.name
        self.category = category


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)


engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
