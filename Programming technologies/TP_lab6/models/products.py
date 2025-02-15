from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cost = Column(Integer)
    supplier = Column(String, ForeignKey('suppliers.id'))
    order = relationship('Order')
    review = relationship('Review')

    def __repr__(self):
        return f'Товар [ID: {self.id}, Название: {self.name}, Стоимость: {self.cost}]'
