from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


#       file _init_.py: Создание движка и сессии.
# Создание экземпляра движка для подключения к SQLite базе данных в памяти
engine = create_engine('sqlite:///example.db')
Base = declarative_base()

# Создание сессии для взаимодействия с базой данных
Session = sessionmaker(bind=engine)
session = Session()








# end