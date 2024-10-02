from xxlimited_35 import error

from sqlalchemy.orm import Session
from Infrastructure.Repositories.TipoCombustivelRepository import TipoCombustivelRepository


class ConsultaTipoCombustivelUseCase:
    def __init__(self, db: Session):
        self.repo = TipoCombustivelRepository(db)

    def execute(self, GetTipoCombustivel):
        try:
            return self.repo.get(GetTipoCombustivel)
        except:
            print(error)
            return error