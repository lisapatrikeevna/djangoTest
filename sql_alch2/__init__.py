from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# pip install pymysql
# pip install sqlalchemy


# engine = create_engine('mysql+pymysql://ich1:ich1_password_ilovedbs@mysql.itcareerhub.de:3306/310524ptm_lisa')
# engine = create_engine('mysql+pymysql://root:parhat1994@localhost:3306/data_1')
engine = create_engine('sqlite:///example.db')

Base = declarative_base()