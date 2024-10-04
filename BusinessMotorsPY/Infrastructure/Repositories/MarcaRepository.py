import logging
from Domain.Entities.Marca import Marca

logger = logging.getLogger(__name__)

class MarcaRepository:
    def __init__(self, db):
        self.db = db

    def get(self, id: int):
        return self.db.query(Marca).filter(Marca.Id == id).first()

    def insert(self, marca: Marca):
        try:
            self.db.add(marca)
            self.db.commit()
            self.db.refresh(marca)
            return marca
        except Exception as ex:
            self.db.rollback()
            logger.error(f"Erro ao inserir marca. Exception: {ex}")
            raise ex