import logging
from Domain.Entities.Marca import Marca

logger = logging.getLogger(__name__)

class MarcaRepository:
    def __init__(self, db):
        self.db = db

    async def get(self, id: int):
        try:
            result = self.db.execute(
                self.db.query(Marca).filter(Marca.Id == id)
            )
            return result.scalar_one_or_none()
        except Exception as e:
            print(f"Exception: {e}")

    async def insert(self, marca: Marca):
        try:
            self.db.add(marca)
            self.db.commit()
            self.db.refresh(marca)
            return marca
        except Exception as ex:
            self.db.rollback()
            logger.error(f"Erro ao inserir marca. Exception: {ex}")
            raise ex