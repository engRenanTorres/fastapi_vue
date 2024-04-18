from fastapi import FastAPI
from routers import router
#uvicorn main:app --reload

app = FastAPI()
app.include_router(router=router)

@app.get("/oi")
def Oi():
    return "oi"
