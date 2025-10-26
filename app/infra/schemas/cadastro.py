from typing import List, Optional
from beanie import Document

class CadastroInput(Document):
    nome: str
    senha: str
    floatLis: Optional[List[str]] = None
     
    class Settings:
        name = 'cadastros'