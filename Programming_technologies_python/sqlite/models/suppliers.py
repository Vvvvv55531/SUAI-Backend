from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.database import Base


class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(String)
    product = relationship('Product')

    def __repr__(self):
        return f'Поставщик [ID: {self.id}, Название: {self.name}, Номер телефона: {self.number}]'
