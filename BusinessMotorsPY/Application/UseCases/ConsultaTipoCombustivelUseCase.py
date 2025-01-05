from xxlimited_35 import error

from fastapi import Depends
from Infrastructure.Repositories.TipoCombustivelRepository import TipoCombustivelRepository


class ConsultaTipoCombustivelUseCase:
    def __init__(self, tipoCombustivelRepository: TipoCombustivelRepository = Depends()):
        self.repo = tipoCombustivelRepository

    def execute(self, GetTipoCombustivel):
        try:
            return self.repo.get(GetTipoCombustivel)
        except:
            print(error)
            return error