import logging
from Domain.Entities.Marca import Marca

logger = logging.getLogger(__name__)

class MarcaRepository:
    def __init__(self, db):
        self.db = db

    async def get(self, id: int):
        result = self.db.execute(
            self.db.query(Marca).filter(Marca.Id == id).first()
        )
        return result.scalar()

    async def insert(self, marca: Marca):
        try:
            self.db.add(marca)
            await self.db.commit()
            await self.db.refresh(marca)
            return marca
        except Exception as ex:
            await self.db.rollback()
            logger.error(f"Erro ao inserir marca. Exception: {ex}")
            raise ex