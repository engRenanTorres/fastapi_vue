from typing import List, Optional
from pydantic import BaseModel

class CadastroCreate(BaseModel):
    nome: str
    senha: str
    floatLis: Optional[List[str]] = []
