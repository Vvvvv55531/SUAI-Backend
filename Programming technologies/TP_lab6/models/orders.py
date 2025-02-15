from sqlalchemy import Column, Integer, String, ForeignKey

from models.database import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    quantity = Column(Integer)
    product = Column(String, ForeignKey('products.id'))

    def __repr__(self):
        return f'Заказ [ID: {self.id}, Дата: {self.date}, Товар: {self.product}, Количество: {self.quantity}]'
