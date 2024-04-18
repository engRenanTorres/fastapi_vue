from os import getenv
import requests
from fastapi import HTTPException

uri = getenv("API_CEP")

def sync_request(cep: str):
    url = f"{uri}/{cep}/json/"
    print(url)

    try:
        response = requests.get(url)
    except Exception as error:
        raise HTTPException(status_code=500,detail=error)
    
    data = response.json()

    return data