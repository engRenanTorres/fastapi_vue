from typing import List
from beanie import Document

class CadastroInput(Document):
    nome: str
    senha: str
    floatLis: List[str]
     
    class Settings:
        name = 'cadastros'