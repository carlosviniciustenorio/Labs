from fastapi import Depends
from sqlalchemy.orm import Session
from Infrastructure.Database.db import get_db

from Domain.Entities.TipoCombustivel import TipoCombustivel

class TipoCombustivelRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, entity):
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def get(self, id: int):
        return self.db.query(TipoCombustivel).filter(TipoCombustivel.Id == id).first()