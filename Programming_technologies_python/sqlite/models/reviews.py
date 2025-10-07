from sqlalchemy import Column, Integer, String, ForeignKey

from models.database import Base


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    grade = Column(Integer)
    product = Column(String, ForeignKey('products.id'))

    def __repr__(self):
        return f'Оценка [ID: {self.id}, Товар: {self.product}, Оценка: {self.grade}]'
