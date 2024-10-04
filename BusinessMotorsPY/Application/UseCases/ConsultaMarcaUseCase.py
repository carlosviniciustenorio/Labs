from sqlalchemy.orm import Session

from Infrastructure.Repositories.MarcaRepository import MarcaRepository


class ConsultaMarcaUseCase:
    def __init__(self, db: Session):
        self.repo = MarcaRepository(db)

    def execute(self, id):
        return self.repo.get(id)