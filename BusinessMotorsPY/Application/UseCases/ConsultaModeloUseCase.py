import logging

from fastapi import Depends
from Infrastructure.Repositories.ModeloRepository import ModeloRepository
logger = logging.getLogger(__name__)

class ConsultaModeloUseCase:
    def __init__(self, modeloRepository: ModeloRepository = Depends()):
        self.modeloRepository = modeloRepository

    async def execute(self, id: int):
        try:
            return await self.modeloRepository.get(id)
        except Exception as ex:
            logger.error(f"Erro ao consultar modelo. Exception:{ex}")
            raise ex