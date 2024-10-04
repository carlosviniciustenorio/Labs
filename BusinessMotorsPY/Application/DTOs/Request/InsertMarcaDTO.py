from pydantic import BaseModel

class InsertMarcaDTO(BaseModel):
    Descricao: str

    class Config:
        arbitrary_types_allowed = True