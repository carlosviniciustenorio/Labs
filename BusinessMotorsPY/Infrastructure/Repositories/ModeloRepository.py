import logging

from Domain.Entities.Modelo import Modelo
logger = logging.getLogger(__name__)

class ModeloRepository:
    def __init__(self, db):
        self.db = db

    async def get(self, id):
        result = self.db.execute(
            self.db.query(Modelo).filter(Modelo.Id == id)
        )
        return result.scalar_one_or_none()

    async def insert(self, modelo):
        try:
            self.db.add(modelo)
            self.db.commit()
            self.db.refresh(modelo)
            return modelo
        except Exception as e:
            logger.error(f"Erro ao cadastrar modelo. Exception: {e}")
            self.db.rollback()
            raise e