from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from __init__ import Base, engine


#       file models.py: Определение моделей.
# 1: Создайте экземпляр движка для подключения к SQLite базе данных в памяти.
# 2: Создайте сессию для взаимодействия с базой данных, используя созданный движок.
# 3: Определите модель продукта Product со следующими типами колонок:
# id: числовой идентификатор
# name: строка (макс. 100 символов)
# price: числовое значение с фиксированной точностью
# in_stock: логическое значение
# Задача 4: Определите связанную модель категории Category со следующими типами колонок:
# id: числовой идентификатор
# name: строка (макс. 100 символов)
# description: строка (макс. 255 символов)
# Задача 5: Установите связь между таблицами Product и Category с помощью колонки category_id.

class Product(Base):
    __tablename__ = 'produkt'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    in_stock = Column(Boolean, default=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    # category = relationship('Category', backref='produkt')
    category = relationship('Category', back_populates='products')


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    products = relationship('Product', back_populates='category')

# Create all tables
Base.metadata.create_all(engine)
















# end
