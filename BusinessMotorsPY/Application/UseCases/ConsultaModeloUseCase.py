import logging
from sqlalchemy.orm import Session

from Infrastructure.Repositories.ModeloRepository import ModeloRepository
logger = logging.getLogger(__name__)

class ConsultaModeloUseCase:
    def __init__(self, db: Session):
        self.modeloRepository = ModeloRepository(db)

    async def execute(self, id: int):
        try:
            return await self.modeloRepository.get(id)
        except Exception as ex:
            logger.error(f"Erro ao consultar modelo. Exception:{ex}")
            raise ex