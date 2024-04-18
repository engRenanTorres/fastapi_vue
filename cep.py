from os import getenv
import requests
import aiohttp
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

async def async_request(cep: str):
    url = f"{uri}/{cep}/json/"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                print(data)
                return data
    except Exception as error:
        raise HTTPException(status_code=500,detail=error)
