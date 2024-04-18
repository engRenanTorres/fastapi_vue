from fastapi import APIRouter
from cep import sync_request

router = APIRouter()

@router.get("/endereco/{cep}")
def converter(cep: str):
    result = sync_request(cep)
    return result

@router.get("/query")
def converter(query: str):
    return query