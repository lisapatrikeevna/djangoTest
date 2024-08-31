from models import Category, Product
from __init__ import session

#       file hw4.py: Наполнение данными и выполнение задач.
# Задача 1: Наполнение данными
# Добавьте в базу данных следующие категории и продукты
# Добавление категорий: Добавьте в таблицу categories следующие категории:
# Название: "Электроника", Описание: "Гаджеты и устройства."
# Название: "Книги", Описание: "Печатные книги и электронные книги."
# Название: "Одежда", Описание: "Одежда для мужчин и женщин."
# Добавление продуктов: Добавьте в таблицу products следующие продукты, убедившись, что каждый продукт связан с соответствующей категорией:
# Название: "Смартфон", Цена: 299.99, Наличие на складе: True, Категория: Электроника
# Название: "Ноутбук", Цена: 499.99, Наличие на складе: True, Категория: Электроника
# Название: "Научно-фантастический роман", Цена: 15.99, Наличие на складе: True, Категория: Книги
# Название: "Джинсы", Цена: 40.50, Наличие на складе: True, Категория: Одежда
# Название: "Футболка", Цена: 20.00, Наличие на складе: True, Категория: Одежда
# Задача 2: Чтение данных
# Извлеките все записи из таблицы categories. Для каждой категории извлеките и выведите все связанные с ней продукты, включая их названия и цены.
# Задача 3: Обновление данных
# Найдите в таблице products первый продукт с названием "Смартфон". Замените цену этого продукта на 349.99.
# Задача 4: Агрегация и группировка
# Используя агрегирующие функции и группировку, подсчитайте общее количество продуктов в каждой категории.
# Задача 5: Группировка с фильтрацией
# Отфильтруйте и выведите только те категории, в которых более одного продукта.


listCategories = [{"id": 1, "name": "Электроника", "description": "Гаджеты и устройства"},
                  {"id": 2, "name": "Книги", "description": "Печатные книги и электронные книги"},
                  {"id": 3, "name": "Одежда", "description": "Одежда для мужчин и женщин"}]
listProducts = [{"id": 1, "name": "Смартфон", "price": 299.99, "in_stock": True, "category_id": 1},
                {"id": 2, "name": "Ноутбук", "price": 499.99, "in_stock": True, "category_id": 1},
                {"id": 3, "name": "Научно-фантастический роман", "price": 15.99, "in_stock": True, "category_id": 2},
                {"id": 4, "name": "Джинсы", "price": 40.50, "in_stock": True, "category_id": 3},
                {"id": 5, "name": "Футболка", "price": 20.00, "in_stock": True, "category_id": 3}]

resCat = [Category(id=cat["id"], name=cat["name"], description=cat["description"]) for cat in listCategories]
# session.add_all(resCat)

resProd = [Product(id=prod["id"], name=prod["name"], price=prod["price"], in_stock=prod["in_stock"], category_id=prod["category_id"]) for prod in listProducts]
# session.add_all(resProd)

# session.commit()

category=session.query(Category)
# produkts=session.query(Product)
for c in category:
    print("categoryName: ", c.name)
    print("description: ", c.description)
    for p in c.products:
        print(f"productName: {p.name}-{p.price}$")

    print("\n")


product= session.query(Product).filter_by(name="Смартфон").first()
print(product.name, product.price, product.category_id)
if product:
    product.price=349.99
    session.commit()

print(product.name, product.price, product.category_id)

for c in category:
    countProd=len(c.products)
    print(c.name ,":",countProd)


for c in category:
    countProd=len(c.products)
    if countProd>1:
        print(c.name ,":",countProd)









