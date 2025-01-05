from fastapi import APIRouter, Depends
from Application.UseCases.ConsultaTipoCombustivelUseCase import ConsultaTipoCombustivelUseCase

router = APIRouter()

@router.get("/tiposcombustiveis/{id}", status_code=200, summary="Consulta Tipo de Combustivel")
def get_tipo_combustivel(id: int, use_case: ConsultaTipoCombustivelUseCase = Depends(ConsultaTipoCombustivelUseCase)):
    return use_case.execute(id)