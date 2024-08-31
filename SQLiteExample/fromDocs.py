from typing import List, Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


# file
# Это Engineфабрика , которая может создавать для нас новые соединения с базой данных
from sqlalchemy import create_engine

engine = create_engine("sqlite://", echo=True)
Base.metadata.create_all(engine)

# file
# Создание объектов и сохранение
from sqlalchemy.orm import Session

with Session(engine) as session:
    spongebob = User(name="spongebob", fullname="Spongebob Squarepants", addresses=[Address(email_address="spongebob@sqlalchemy.org")], )
    sandy = User(name="sandy", fullname="Sandy Cheeks", addresses=[Address(email_address="sandy@sqlalchemy.org"), Address(email_address="sandy@squirrelpower.org"), ], )
    patrick = User(name="patrick", fullname="Patrick Star")
    session.add_all([spongebob, sandy, patrick])  # session.commit()

# file
# Простой ВЫБОР
# Метод, который часто бывает полезен это метод Session.scalars(),
# который вернет ScalarResultобъект, который будет итерировать по выбранным нами объектам
from sqlalchemy import select

session = Session(engine)

stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

for user in session.scalars(stmt):
    print(user)

# ВЫБРАТЬ с помощью JOIN
# stmt = (select(Address).join(Address.user).where(User.name == "sandy").where(Address.email_address == "sandy@sqlalchemy.org"))
# sandy_address = session.scalars(stmt).one()
# sandy_address


# Внести изменения

# stmt = select(User).where(User.name == "patrick")
# patrick = session.scalars(stmt).one()
# patrick.addresses.append(Address(email_address="patrickstar@sqlalchemy.org"))
# sandy_address.email_address = "sandy_cheeks@sqlalchemy.org"

# session.commit()


   # file
# from __future__ import annotations
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Parent(Base):
    __tablename__ = "parent_table"

    id = mapped_column(Integer, primary_key=True)
    children = relationship("Child", back_populates="parent")


class Child(Base):
    __tablename__ = "child_table"

    id = mapped_column(Integer, primary_key=True)
    parent_id = mapped_column(ForeignKey("parent_table.id"))
    parent = relationship("Parent", back_populates="children")





