from fastapi import APIRouter

router = APIRouter()

@router.get("/converter/{moeda_corrente}")
def converter(moeda_corrente: str):
    return moeda_corrente

@router.get("/query")
def converter(query: str):
    return query