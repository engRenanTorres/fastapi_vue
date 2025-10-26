from pydantic import BaseModel
from typing import List

class CadastroInput(BaseModel):
    nome: str
    senha: str
    floatLis: List[str]