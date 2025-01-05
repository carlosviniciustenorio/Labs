from fastapi import Depends

from Application.DTOs.Request.InsertModeloDTO import InsertModeloDTO
from Domain.Entities.Modelo import Modelo
from Infrastructure.Repositories.MarcaRepository import MarcaRepository
from Infrastructure.Repositories.ModeloRepository import ModeloRepository


class CadastraModeloUseCase:
    def __init__(self,
                 modeloRepository: ModeloRepository = Depends(),
                 marcaRepository: MarcaRepository = Depends()
                 ):
        self.modeloRepository = modeloRepository
        self.marcaRepository = marcaRepository

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