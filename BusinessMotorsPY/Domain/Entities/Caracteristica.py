from sqlalchemy import Column, Integer, String

from Infrastructure.Database.base import Base


class Caracteristica(Base):
    __tablename__ = 'Caracteristica'
    Id = Column(Integer, primary_key=True)
    Descricao = Column(String, maxsize=100)