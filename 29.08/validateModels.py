import datetime

from pydantic import BaseModel, field_validator, Field, EmailStr


# Создайте модель Event, которая включает поля:
# title (строка),
# date (дата и время события),
# location (строка).
# Добавьте валидацию, чтобы дата события не была в прошлом.

class Event(BaseModel):
    title: str
    date: datetime
    location: str

    @field_validator("date")
    def date_valid(cls, value):
        if value < datetime.now():
            raise ValueError('Value incorect')
        else:
            return value


future_event = Event(title="New Year Party", date=datetime.now() + datetime.timedelta(days=30), location="New York")
print(future_event)


# Определите модель UserProfile с полями:
# username (строка),
# password (строка),
# email (строка с валидацией email).
# Используйте Field для добавления описаний и настройки валидации пароля (должен быть не менее 8 символов).

class UserProfile(BaseModel):
    userName: str
    password: str = Field(..., min_length=8, max_length=128, description='Your password')
    email: EmailStr = Field(..., description='Your email')


user_profile1 = UserProfile(username='Jon doe', password='12345678', email='john@gmail.com')
print(user_profile1)
