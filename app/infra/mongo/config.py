from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, Indexed
from app.infra.schemas.cadastro import CadastroInput
from os import getenv


class MongoConfig():

    uri: str 
    db_name: str
    client: AsyncIOMotorClient
    def __init__(self):
        self.uri = getenv("MONGO_KEY")
        self.db_name = getenv("DB_NAME")
        if self.uri is None or self.db_name is None:
            raise Exception("DB key is not set")
        self.client = AsyncIOMotorClient(self.uri)


    async def init(self):
        await init_beanie(
            database=self.client[self.db_name],
            document_models=[CadastroInput]
            )