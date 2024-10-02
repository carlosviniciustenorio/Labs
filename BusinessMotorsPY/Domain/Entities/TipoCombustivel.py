from sqlalchemy import Column, ForeignKey, String, Integer

from Infrastructure.Database.db import Base


class TipoCombustivel(Base):
    __tablename__ = 'TipoCombustivel'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Descricao = Column(String(255))