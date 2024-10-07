from pydantic import BaseModel

class InsertModeloDTO(BaseModel):
    Descricao: str
    AnoModelo: int
    AnoFabricacao: int
    MarcaId: int