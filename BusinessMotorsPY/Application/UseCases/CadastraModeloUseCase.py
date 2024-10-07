from sqlalchemy.orm import Session

from Application.DTOs.Request.InsertModeloDTO import InsertModeloDTO
from Domain.Entities.Modelo import Modelo
from Infrastructure.Repositories.MarcaRepository import MarcaRepository
from Infrastructure.Repositories.ModeloRepository import ModeloRepository


class CadastraModeloUseCase:
    def __init__(self, db: Session):
        self.modeloRepository = ModeloRepository(db)
        self.marcaRepository = MarcaRepository(db)

    async def execute(self, modeloDTO: InsertModeloDTO):
        marca = self.marcaRepository.get(modeloDTO.MarcaId)

        if(marca is None):
            raise Exception("Marca is not found")

        modelo = Modelo(
            Descricao = modeloDTO.Descricao,
            AnoModelo = modeloDTO.AnoModelo,
            AnoFabricacao = modeloDTO.AnoFabricacao,
            MarcaId = modeloDTO.MarcaId
        )
        return await self.modeloRepository.insert(modelo)