from typing import List
from fastapi import APIRouter, Depends, HTTPException, Path,Query
from app.api.utils.http_status import httpStatus
from app.entities.dtos.cadastro_create import CadastroCreate
from app.entities.dtos.cadastro_response import CadastroResponse
from app.entities.dtos.cadastro_update import CadastroUpdate
from app.infra.repositories.cadastro_repositorie import CadastroRepository, get_cadastro_repository


cadastro_router = APIRouter()

@cadastro_router.get("/", response_model=List[CadastroResponse])
async def get_all_cadastros(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    repo: CadastroRepository = Depends(get_cadastro_repository)
):
    """
    Listar todos os cadastros com paginação
    """
    cadastros = await repo.get_all(skip=skip, limit=limit)
    return [
        CadastroResponse(
            id=str(cadastro.id),
            nome=cadastro.nome,
            senha=cadastro.senha,
            floatLis=cadastro.floatLis
        )
        for cadastro in cadastros
    ]


@cadastro_router.get("/{cadastro_id}", response_model=CadastroResponse)
async def get_cadastro_by_id(
    cadastro_id: str,
    repo: CadastroRepository = Depends(get_cadastro_repository)
):
    """
    Buscar cadastro por ID
    """
    cadastro = await repo.get_by_id(cadastro_id)
    if not cadastro:
        raise HTTPException(
            status_code=httpStatus.HTTP_404_NOT_FOUND,
            detail=f"Cadastro com ID {cadastro_id} não encontrado"
        )
    
    return CadastroResponse(
        id=str(cadastro.id),
        nome=cadastro.nome,
        senha=cadastro.senha,
        floatLis=cadastro.floatLis
    )


@cadastro_router.get("/search/", response_model=List[CadastroResponse])
async def search_cadastros(
    q: str = Query(..., min_length=1),
    repo: CadastroRepository = Depends(get_cadastro_repository)
):
    """
    Buscar cadastros por nome (busca parcial)
    """
    cadastros = await repo.search(q)
    return [
        CadastroResponse(
            id=str(cadastro.id),
            nome=cadastro.nome,
            senha=cadastro.senha,
            floatLis=cadastro.floatLis
        )
        for cadastro in cadastros
    ]


@cadastro_router.post("/", response_model=CadastroResponse, status_code=httpStatus.HTTP_201_CREATED)
async def create_cadastro(
    cadastro_data: CadastroCreate,
    repo: CadastroRepository = Depends(get_cadastro_repository)
):
    """
    Criar novo cadastro
    """
    # Verificar se já existe
    if await repo.exists(cadastro_data.nome):
        raise HTTPException(
            status_code=httpStatus.HTTP_400_BAD_REQUEST,
            detail=f"Cadastro com nome '{cadastro_data.nome}' já existe"
        )
    
    cadastro = await repo.create(
        nome=cadastro_data.nome,
        senha=cadastro_data.senha,
        float_list=cadastro_data.floatLis
    )
    
    return CadastroResponse(
        id=str(cadastro.id),
        nome=cadastro.nome,
        senha=cadastro.senha,
        floatLis=cadastro.floatLis
    )


@cadastro_router.put("/{cadastro_id}", response_model=CadastroResponse)
async def update_cadastro(
    cadastro_id: str,
    cadastro_data: CadastroUpdate,
    repo: CadastroRepository = Depends(get_cadastro_repository)
):
    """
    Atualizar cadastro completo
    """
    cadastro = await repo.update(
        cadastro_id=cadastro_id,
        nome=cadastro_data.nome,
        senha=cadastro_data.senha,
        float_list=cadastro_data.floatLis
    )
    
    if not cadastro:
        raise HTTPException(
            status_code=httpStatus.HTTP_404_NOT_FOUND,
            detail=f"Cadastro com ID {cadastro_id} não encontrado"
        )
    
    return CadastroResponse(
        id=str(cadastro.id),
        nome=cadastro.nome,
        senha=cadastro.senha,
        floatLis=cadastro.floatLis
    )


@cadastro_router.patch("/{cadastro_id}", response_model=CadastroResponse)
async def partial_update_cadastro(
    cadastro_id: str,
    cadastro_data: CadastroUpdate,
    repo: CadastroRepository = Depends(get_cadastro_repository)
):
    """
    Atualizar parcialmente um cadastro (apenas campos enviados)
    """
    # Converter para dict removendo valores None
    update_data = cadastro_data.model_dump(exclude_unset=True)
    
    if not update_data:
        raise HTTPException(
            status_code=httpStatus.HTTP_400_BAD_REQUEST,
            detail="Nenhum campo para atualizar foi fornecido"
        )
    
    cadastro = await repo.update_partial(cadastro_id, **update_data)
    
    if not cadastro:
        raise HTTPException(
            status_code=httpStatus.HTTP_404_NOT_FOUND,
            detail=f"Cadastro com ID {cadastro_id} não encontrado"
        )
    
    return CadastroResponse(
        id=str(cadastro.id),
        nome=cadastro.nome,
        senha=cadastro.senha,
        floatLis=cadastro.floatLis
    )


@cadastro_router.delete("/{cadastro_id}", status_code=httpStatus.HTTP_204_NO_CONTENT)
async def delete_cadastro(
    cadastro_id: str,
    repo: CadastroRepository = Depends(get_cadastro_repository)
):
    """
    Deletar cadastro por ID
    """
    deleted = await repo.delete(cadastro_id)
    
    if not deleted:
        raise HTTPException(
            status_code=httpStatus.HTTP_404_NOT_FOUND,
            detail=f"Cadastro com ID {cadastro_id} não encontrado"
        )
    
    return None


@cadastro_router.get("/count/total")
async def count_cadastros(
    repo: CadastroRepository = Depends(get_cadastro_repository)
):
    """
    Contar total de cadastros
    """
    total = await repo.count()
    return {"total": total}

