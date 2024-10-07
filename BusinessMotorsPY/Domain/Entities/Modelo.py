from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from Infrastructure.Database.base import Base


class Modelo(Base):
    __tablename__ = 'Modelo'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Descricao = Column(String)
    AnoModelo = Column(Integer)
    AnoFabricacao = Column(Integer)
    MarcaId = Column(Integer, ForeignKey('Marca.Id'))

    marca = relationship("Marca", back_populates="modelos")