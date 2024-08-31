from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# Создание экземпляра движка для подключения к SQLite базе данных в памяти
engine = create_engine('sqlite:///example.db')
Base = declarative_base()
