from sqlalchemy.orm import Session

from Application.DTOs.Request.InsertMarcaDTO import InsertMarcaDTO
from Domain.Entities.Marca import Marca

from Infrastructure.Repositories.MarcaRepository import MarcaRepository


class CadastraMarcaUseCase:
    def __init__(self, db: Session):
        self.repo = MarcaRepository(db)

    async def execute(self, marcaDTO: InsertMarcaDTO):
        marca = Marca(Descricao = marcaDTO.Descricao)
        return await self.repo.insert(marca)