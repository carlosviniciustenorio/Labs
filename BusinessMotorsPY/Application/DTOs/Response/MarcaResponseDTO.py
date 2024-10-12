from pydantic import BaseModel

class MarcaResponseDTO(BaseModel):
    id: int
    descricao: str
