from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    Text,
    Column,
    Integer,
    String,
    Numeric,
    Boolean)
from sql_alch import engine, Base
from sqlalchemy.orm import relationship
# Определение модели продукта
# Определите модель Product с различными
# типами колонок:
# id (числовой идентификатор)
# name (строковый)
# price (точный дробный)
# in_stock (логический)

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    price = Column(Numeric(10, 2))
    in_stock = Column(Boolean)
    category = relationship("category", back_populates="product")
    description = Column(Text)


# Определение связанной модели
# категории продукта
# Определите модель Category, которая будет
# связана с моделью Product для организации
# продуктов по категориям.
#
# Каждый продукт должен принадлежать
# одной категории. Category должна включать
# колонки:
# id (числовой идентификатор
# name (строковый
# description (строковый)


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(Text)
    products = relationship('Product', back_populates='category')#created link in product
    # products = relationship('Product', backref='category')#created link in product only in one column
























