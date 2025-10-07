from models.database import create_db, Session
from models.products import Product
from models.suppliers import Supplier
from models.orders import Order
from models.reviews import Review


def create_database(load_fake_data: bool = True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session: Session):

    products = [Product(name='Рассада помидор', cost='299', supplier=1),
                Product(name='Семена цветов', cost='99', supplier=1),
                Product(name='Горшки для растений', cost='149', supplier=2)]

    for product in range(len(products)):
        session.add(products[product])

    suppliers = [Supplier(name='Семенная компания "Зеленый мир"', number='8988-231-86-71'),
                 Supplier(name='ООО "Горшочек"', number='8918-371-87-77')]

    for supplier in range(len(suppliers)):
        session.add(suppliers[supplier])

    orders = [Order(date='13.05.2023', quantity=2, product=1),
              Order(date='01.05.2023', quantity=1, product=1),
              Order(date='20.04.2023', quantity=3, product=2),
              Order(date='05.04.2023', quantity=2, product=2),
              Order(date='01.04.2023', quantity=1, product=3)]

    for order in range(len(orders)):
        session.add(orders[order])

    reviews = [Review(grade=4.0, product=1),
               Review(grade=4.1, product=1),
               Review(grade=4.9, product=2),
               Review(grade=4.5, product=2),
               Review(grade=4.7, product=2),
               Review(grade=3.9, product=3),
               Review(grade=5.0, product=3)]

    for review in range(len(reviews)):
        session.add(reviews[review])

    session.commit()
    session.close()
