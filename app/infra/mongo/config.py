from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, Indexed
from app.infra.schemas.cadastro import CadastroInput
from os import getenv
from pydantic import BaseModel

class MongoConfig(BaseModel):

    uri: str 
    client: AsyncIOMotorClient
    def __init__(self):
        self.uri = getenv("MONGO_KEY")
        if self.uri is None:
            raise Exception("DB key is not set")
        self.client = AsyncIOMotorClient(self.uri)


    async def init(self):
        await init_beanie(
            database=self.client.my_db, 
            document_models=[CadastroInput]
            )