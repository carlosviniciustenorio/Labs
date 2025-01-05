from fastapi import APIRouter, Depends

from Application.DTOs.Request.InsertMarcaDTO import InsertMarcaDTO
from Application.UseCases.CadastraMarcaUseCase import CadastraMarcaUseCase
from Application.UseCases.ConsultaMarcaUseCase import ConsultaMarcaUseCase

router = APIRouter()

@router.get("/marcas/{id}", status_code=200, summary="Consulta Marca")
async def get_marca(id: int, use_case: ConsultaMarcaUseCase = Depends(ConsultaMarcaUseCase)):
    return await use_case.execute(id)

@router.post("/marcas/", status_code=201, summary="Cadastrar Marca")
async def post_marca(marcaDTO: InsertMarcaDTO, use_case: CadastraMarcaUseCase = Depends(CadastraMarcaUseCase)):
    return await use_case.execute(marcaDTO)
