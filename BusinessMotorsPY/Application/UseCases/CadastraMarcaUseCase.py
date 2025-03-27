from fastapi import Depends

from Application.DTOs.Request.InsertMarcaDTO import InsertMarcaDTO
from Domain.Entities.Marca import Marca

from Infrastructure.Repositories.MarcaRepository import MarcaRepository


class CadastraMarcaUseCase:
    def __init__(self, marcaRepository: MarcaRepository = Depends()):
        self.marcaRepository = marcaRepository

    async def execute(self, marcaDTO: InsertMarcaDTO):
        marca = Marca(Descricao = marcaDTO.Descricao)
        return await self.marcaRepository.insert(marca)