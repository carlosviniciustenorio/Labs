from fastapi import APIRouter, Depends

from Application.DTOs.Request.InsertModeloDTO import InsertModeloDTO
from Application.UseCases.CadastraModeloUseCase import CadastraModeloUseCase
from Application.UseCases.ConsultaModeloUseCase import ConsultaModeloUseCase

router = APIRouter()

@router.get("/modelos/{id}", status_code=200, summary="Consulta Modelo")
async def get_modelo(id: int, use_case: ConsultaModeloUseCase = Depends(ConsultaModeloUseCase)):
    return await use_case.execute(id)

@router.post("/modelos/", status_code=200, summary="Cadastra Modelo")
async def post_modelo(modelo: InsertModeloDTO, use_case: CadastraModeloUseCase = Depends(CadastraModeloUseCase)):
    return await use_case.execute(modelo)
