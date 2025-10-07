import os

from models.database import DATABASE_NAME, Session
import create_database as db_creator

from models.products import Product
from models.suppliers import Supplier
from models.orders import Order
from models.reviews import Review

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()
    for it in session.query(Product):
        print(it)
    print('*' * 30)
    for it in session.query(Supplier):
        print(it)
    print('*' * 30)
    for it in session.query(Order):
        print(it)
    print('*' * 30)
    for it in session.query(Review):
        print(it)
    print('*' * 30)
    for it in session.query(Product).filter(Product.id < 3):
        print(it)
    print('*' * 30)
    for it in session.query(Supplier).filter(Supplier.id > 1):
        print(it)
    print('*' * 30)
    for it in session.query(Order).filter(Order.id == 3):
        print(it)
    print('*' * 30)
    for it in session.query(Review).filter(Review.id >= 3):
        print(it)
    print('*' * 30)
    for it in session.query(Product).filter(Product.name == 'Рассада помидор'):
        print(it)
    print('*' * 30)
    for it in session.query(Order).filter(Order.date == '13.05.2023'):
        print(it)
    print('*' * 30)
