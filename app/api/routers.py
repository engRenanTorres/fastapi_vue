from fastapi import APIRouter, Path,Query
from app.use_cases.cep import sync_request,async_request
from app.infra.schemas.cadastro import CadastroInput

router = APIRouter(prefix="/api")

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

@router.get("/cadastro/")
async def get_users():
    cadastros = await CadastroInput.find_all().to_list()
    return cadastros