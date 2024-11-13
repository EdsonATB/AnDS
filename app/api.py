from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from app.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)

# Adicionando o middleware CORSMiddleware para configurar o CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    # Retornando JSON ao invés de HTML
    return JSONResponse

#Para iniciar a api abra o terminal e digite uvicorn app.main:app --reload
#Para iniciar a api abra o terminal e digite uvicorn app.api:app --reload
