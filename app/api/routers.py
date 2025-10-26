from fastapi import APIRouter, Path,Query
from app.use_cases.cep import sync_request,async_request
from app.infra.schemas.cadastro import CadastroInput
from app.api.controllers.cadastro_constroller import cadastro_router

router = APIRouter(prefix="/api")

router.include_router(cadastro_router,prefix="/api/cadastro",tags=["Cadastro"])

@router.get("/endereco/{cep}")
def converter(cep: str = Path(regex="^\d{8}$", min_length=8)):
    result = sync_request(cep)
    return result

@router.get("/aendereco")
async def async_end(
    cep: str = Query(regex="^\d{8}$", min_length=8),
    nome: str = Query(description="nome do proprietario")
    ):
    result = await async_request(cep)
    return result

@router.get("/query")
def converterQuery(query: str):
    return query