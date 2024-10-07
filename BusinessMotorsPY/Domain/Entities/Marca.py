from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from Infrastructure.Database.base import Base


class Marca(Base):
    __tablename__ = 'Marca'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Descricao = Column(String)
    modelos = relationship("Modelo", back_populates="marca")