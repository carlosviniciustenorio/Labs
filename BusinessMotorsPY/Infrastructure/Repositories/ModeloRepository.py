import logging

from Domain.Entities.Modelo import Modelo
logger = logging.getLogger(__name__)

class ModeloRepository:
    def __init__(self, db):
        self.db = db

    async def get(self, id):
        result = await self.db.execute(
            self.db.query(Modelo).filter(Modelo.Id == id)
        )
        return result.scalar()

    async def insert(self, modelo):
        try:
            self.db.add(modelo)
            await self.db.commit()
            await self.db.refresh(modelo)
            return modelo
        except Exception as e:
            await self.db.rollback()
            logger.error(f"Erro ao cadastrar modelo. Exception: {e}")
            raise e