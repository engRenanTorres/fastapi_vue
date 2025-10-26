from fastapi import FastAPI
from app.routers import router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
#uvicorn main:app --reload

app = FastAPI()
app.include_router(router=router)

@app.get("/oi")
def Oi():
    return "oi"

@app.get("/{full_path:path}")
async def serve_vue(full_path: str):
    # Se o arquivo existe, serve ele
    file_path = os.path.join("app/dist", full_path)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(file_path)
    
    # Caso contrário, serve o index.html (para o Vue Router funcionar)
    return FileResponse("app/dist/index.html")
