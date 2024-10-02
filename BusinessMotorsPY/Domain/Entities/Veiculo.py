from pydantic import BaseModel

class Veiculo(BaseModel):
    id: int
    marca: str
    modelo: str
    anoFabricacao: int
    anoModelo: int
    versao: str
    estaDisponivel: bool
    valor: float