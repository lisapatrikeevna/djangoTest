import logging

from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from models import User
from sql_alch import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

Session = sessionmaker(bind=engine)
session = Session()

# user1 = User(
#     name='Patrick',
#     age=56,
#     email='vladafds@gmail.com'
# )
#
# session.add(user1)
# session.commit()
#
# address1 = Address(
#     user_id=user1.id,
#     description='Apartment',
#     city="LA"
# )
#
# session.add(address1)
# session.commit()

# session.add_all([User(name='Bob', age=22, email='alice@example.com'),
#                  User(name='David', age=27, email='vladafds@gmail.com'),
#                  User(name='Patrick', age=56, email='vladafds@gmail.com'),
#                  User(name='Alice', age=30, email='alice@example.com'),
#                  User(name='Bob', age=45, email='bob@example.com')])
# session.commit()
#
# session.close()
#
# query = session.query(User).filter(User.name == 'Bob').all()
#
# for user in query:
#     print(user.name)


# user = session.query(User).get(2)
# if user:
#     user.age = 35
#     session.commit()

# user = session.query(User).get(1)
# if user:
#     session.delete(user)
#     session.commit()
#     print('user deleted')
# else:
#     print('user not found')


# query = session.query(User)
# for user in query.all():
#     print(user.name, user.email)
#
# query1 = session.query(User).all()
# for user in query1:
#     print(user.name, user.email)


#
# query2 = session.query(User).first()     #retuned ferst res
# print(query2.name, query2.email)
#
# query3 = session.query(User).filter(User.name=="Ann").one()
# print(query3.name, query3.email)

# zapros = session.query(User).filter(User.age > 18).all()
# for stroka in zapros:
#     print(stroka.id, stroka.name, stroka.age)
#
#     # Поиск пользователей, чье имя начинается на "A"
# users = session.query(User).filter(User.name.like('A%')).all()
# for user in users:
#     print(user.id, user.name)
# # Поиск пользователей с ID между 2 и 4
# users = session.query(User).filter(User.id.between(2, 4)).all()
# for user in users:
#     print(user.id, user.name)
# # Поиск пользователей, чьи имена находятся в списке
# names = ["Alice", "Bob"]
# users = session.query(User).filter(User.name.in_(names)).all()
# for user in users:    print(user.id, user.name)


# users = session.query(User).filter(or_(User.age > 20, User.name == "Anna")).all()
# # users = session.query(User).filter(and_(User.age>20, User.age<23)).all()
# for user in users:
#     print(user.id)


# users = session.query(User).filter(not_(User.name == 'Ann')).all()
# for user in users:
#     print(user.id, user.name, user.age)
#
# zapros = session.query(User).order_by(desc(User.age)).all()
# for user in zapros:
#     print(user.id, user.name, user.age)
# zapros = session.query(User).order_by(desc(User.age), User.name).all()
# for user in zapros:
#     print(user.id, user.name, user.age)

# # Подзапрос для вычисления среднего возраста сохраняем в переменную
# average_age_subquery = session.query(func.avg(User.age).label('average_age')).subquery()
# # Основной запрос, использующий подзапрос для фильтрации пользователей
# users = session.query(User).filter(User.age > average_age_subquery).all()
#
# # Выполним подзапрос отдельно для проверки результата
# print(f"Average age is {session.query(average_age_subquery).scalar()}")
# # Выведем отобранные данные
# for user in users:
#     print(user.id, user.name, user.age)


average_ = session.query(func.avg(User.age).label('average')).subquery()

users = session.query(User).filter(User.age > average_).all()

# Выполним подзапрос отдельно для проверки результата
print(f"Average age is {session.query(average_).scalar()}")
# Выведем отобранные данные
for user in users:
    print(user.id, user.name, user.age)







    # engine = create_engine('mysql+pymysql://ich1:ich1_password_ilovedbs@mysql.itcareerhub.de:3306/------)












