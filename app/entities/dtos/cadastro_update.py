from typing import List, Optional
from pydantic import BaseModel


class CadastroUpdate(BaseModel):
    nome: Optional[str] = None
    senha: Optional[str] = None
    floatLis: Optional[List[str]] = None

