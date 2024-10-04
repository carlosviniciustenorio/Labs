from sqlalchemy import Integer, Column, String

from Infrastructure.Database.base import Base


class Marca(Base):
    __tablename__ = 'Marca'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Descricao = Column(String)