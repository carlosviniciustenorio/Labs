from fastapi import FastAPI, HTTPException, Response, Depends
from sqlalchemy.orm import Session
from Application.DTOs.Request import InsertModeloDTO
from Application.DTOs.Request.InsertMarcaDTO import InsertMarcaDTO
from Application.UseCases.CadastraMarcaUseCase import CadastraMarcaUseCase
from Application.UseCases.CadastraModeloUseCase import CadastraModeloUseCase
from Application.UseCases.ConsultaMarcaUseCase import ConsultaMarcaUseCase
from Application.UseCases.ConsultaModeloUseCase import ConsultaModeloUseCase
from Application.UseCases.ConsultaTipoCombustivelUseCase import ConsultaTipoCombustivelUseCase
from Infrastructure.Database.db import get_db

app = FastAPI()

@app.get("/tiposcombustiveis/{id}", status_code=200, summary="Consulta Tipo de Combustivel")
def get_tipo_combustivel(id: int, db: Session = Depends(get_db)):
    consultaTipoCombustivelUseCase = ConsultaTipoCombustivelUseCase(db)
    return consultaTipoCombustivelUseCase.execute(id)

@app.get("/marcas/{id}", status_code=200, summary="Consulta Marca")
async def get_marca(id: int, db: Session = Depends(get_db)):
    useCase = ConsultaMarcaUseCase(db)
    return await useCase.execute(id)

@app.post("/marcas/", status_code=200, summary="Cadastrar Marca")
async def post_marca(marca: InsertMarcaDTO, db: Session = Depends(get_db)):
    useCase = CadastraMarcaUseCase(db)
    return await useCase.execute(marca)

@app.get("/modelos/{id}", status_code=200, summary="Consulta Modelo")
async def get_modelo(id: int, db: Session = Depends(get_db)):
    useCase = ConsultaModeloUseCase(db)
    return await useCase.execute(id)

@app.post("/modelos/", status_code=200, summary="Consulta Modelo")
async def post_modelo(modelo: InsertModeloDTO, db: Session = Depends(get_db)):
    useCase = CadastraModeloUseCase(db)
    return await useCase.execute(modelo)