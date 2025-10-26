# app/repositories/cadastro_repository.py
from typing import List, Optional
from beanie import PydanticObjectId
from app.infra.schemas.cadastro import CadastroInput


class CadastroRepository:
    """
    Repository para operações CRUD com Cadastro usando Beanie
    """
    
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[CadastroInput]:
        """
        Buscar todos os cadastros com paginação
        """
        return await CadastroInput.find_all().skip(skip).limit(limit).to_list()
    
    async def get_by_id(self, cadastro_id: str) -> Optional[CadastroInput]:
        """
        Buscar cadastro por ID
        """
        try:
            return await CadastroInput.get(PydanticObjectId(cadastro_id))
        except Exception:
            return None
    
    async def get_by_nome(self, nome: str) -> Optional[CadastroInput]:
        """
        Buscar cadastro por nome
        """
        return await CadastroInput.find_one(CadastroInput.nome == nome)
    
    async def create(self, nome: str, senha: str, float_list: Optional[List[str]] = None) -> CadastroInput:
        """
        Criar novo cadastro
        """
        cadastro = CadastroInput(
            nome=nome,
            senha=senha,
            floatLis=float_list or []
        )
        await cadastro.insert()
        return cadastro
    
    async def update(self, cadastro_id: str, nome: Optional[str] = None, 
                    senha: Optional[str] = None, float_list: Optional[List[str]] = None) -> Optional[CadastroInput]:
        """
        Atualizar cadastro existente
        """
        cadastro = await self.get_by_id(cadastro_id)
        if not cadastro:
            return None
        
        # Atualizar apenas campos fornecidos
        if nome is not None:
            cadastro.nome = nome
        if senha is not None:
            cadastro.senha = senha
        if float_list is not None:
            cadastro.floatLis = float_list
        
        await cadastro.save()
        return cadastro
    
    async def update_partial(self, cadastro_id: str, **kwargs) -> Optional[CadastroInput]:
        """
        Atualizar parcialmente um cadastro (apenas campos enviados)
        """
        cadastro = await self.get_by_id(cadastro_id)
        if not cadastro:
            return None
        
        # Atualizar usando o método update do Beanie
        await cadastro.set(kwargs)
        return await self.get_by_id(cadastro_id)
    
    async def delete(self, cadastro_id: str) -> bool:
        """
        Deletar cadastro por ID
        """
        cadastro = await self.get_by_id(cadastro_id)
        if not cadastro:
            return False
        
        await cadastro.delete()
        return True
    
    async def delete_by_nome(self, nome: str) -> bool:
        """
        Deletar cadastro por nome
        """
        cadastro = await self.get_by_nome(nome)
        if not cadastro:
            return False
        
        await cadastro.delete()
        return True
    
    async def count(self) -> int:
        """
        Contar total de cadastros
        """
        return await CadastroInput.count()
    
    async def exists(self, nome: str) -> bool:
        """
        Verificar se cadastro existe por nome
        """
        cadastro = await self.get_by_nome(nome)
        return cadastro is not None
    
    async def search(self, query: str) -> List[CadastroInput]:
        """
        Buscar cadastros por texto (nome contém query)
        """
        # Busca case-insensitive
        return await CadastroInput.find(
            {"nome": {"$regex": query, "$options": "i"}}
        ).to_list()


# Função para injeção de dependência
def get_cadastro_repository() -> CadastroRepository:
    return CadastroRepository()