import logging

from sqlalchemy.orm import sessionmaker

from models import User, Address
from sql_alch import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

Session = sessionmaker(bind=engine)
session = Session()

user1 = User(
    name='Patrick',
    age=56,
    email='vladafds@gmail.com'
)

session.add(user1)
session.commit()

address1 = Address(
    user_id=user1.id,
    description='Apartment',
    city="LA"
)


session.add(address1)
session.commit()


session.close()



# user_data = session.query(User).filter(User.id == 1).first()

# session.delete(user_data)
# session.commit()
