from typing import List, Optional
from pydantic import BaseModel


class CadastroResponse(BaseModel):
    id: str
    nome: str
    senha: str
    floatLis: Optional[List[str]] = []

    class Config:
        from_attributes = True