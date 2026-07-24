"""
    This is where the app models are created.
"""

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, relationship


engine = create_engine("sqlite:///model/db/app.db", echo=True)


class Base(DeclarativeBase):
    pass


class ItemObj:
    def __init__(self, item, category):
        self.id = item.id
        self.name = item.name
        self.category = category


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    cat_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)


Base.metadata.create_all(engine)
