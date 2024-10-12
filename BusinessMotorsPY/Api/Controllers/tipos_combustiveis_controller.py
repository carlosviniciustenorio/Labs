from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Application.UseCases.ConsultaTipoCombustivelUseCase import ConsultaTipoCombustivelUseCase
from Infrastructure.Database.db import get_db

router = APIRouter()

@router.get("/tiposcombustiveis/{id}", status_code=200, summary="Consulta Tipo de Combustivel")
def get_tipo_combustivel(id: int, db: Session = Depends(get_db)):
    consultaTipoCombustivelUseCase = ConsultaTipoCombustivelUseCase(db)
    return consultaTipoCombustivelUseCase.execute(id)
