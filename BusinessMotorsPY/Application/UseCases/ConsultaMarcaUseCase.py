import logging

from fastapi import Depends
from Infrastructure.Repositories.MarcaRepository import MarcaRepository

logger = logging.getLogger(__name__)

class ConsultaMarcaUseCase:
    def __init__(self, marcaRepository: MarcaRepository = Depends()):
        self.repo = marcaRepository

    async def execute(self, id):
        try:
            return await self.repo.get(id)
        except Exception as ex:
            logger.error(f"Erro ao consultar modelo. Exception:{ex}")
            raise ex