from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Application import InsertMarcaDTO, CadastraMarcaUseCase, ConsultaMarcaUseCase
from Infrastructure.Database.db import get_db

router = APIRouter()

@router.get("/marcas/{id}", status_code=200, summary="Consulta Marca")
async def get_marca(id: int, db: Session = Depends(get_db)):
    useCase = ConsultaMarcaUseCase(db)
    return await useCase.execute(id)

@router.post("/marcas/", status_code=201, summary="Cadastrar Marca")
async def post_marca(marcaDTO: InsertMarcaDTO, db: Session = Depends(get_db)):
    useCase = CadastraMarcaUseCase(db)
    return await useCase.execute(marcaDTO)
