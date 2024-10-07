import string

from pydantic import BaseModel


class Modelo(BaseModel):
    Descricao: string
    AnoModelo: int
    AnoFabricacao: int
    MarcaId: int

    class Config:
        arbitrary_types_allowed = True