from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Application.DTOs.Request.InsertModeloDTO import InsertModeloDTO
from Application.UseCases.CadastraModeloUseCase import CadastraModeloUseCase
from Application.UseCases.ConsultaModeloUseCase import ConsultaModeloUseCase
from Infrastructure.Database.db import get_db

router = APIRouter()

@router.get("/modelos/{id}", status_code=200, summary="Consulta Modelo")
async def get_modelo(id: int, db: Session = Depends(get_db)):
    useCase = ConsultaModeloUseCase(db)
    return await useCase.execute(id)

@router.post("/modelos/", status_code=200, summary="Cadastra Modelo")
async def post_modelo(modelo: InsertModeloDTO, db: Session = Depends(get_db)):
    useCase = CadastraModeloUseCase(db)
    return await useCase.execute(modelo)
