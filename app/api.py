from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes import router

app = FastAPI()

# Inclui as rotas definidas em routes.py
app.include_router(router)

# Monta o diretório static para servir arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define a rota para a página inicial
@app.get("/")
async def read_index():
    return FileResponse("static/index.html")
