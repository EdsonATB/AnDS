from fastapi import APIRouter, Form
from .main import enviar_texto


router = APIRouter()

@router.post("/pesquisar")
async def receber_texto(pesquisa: str = Form(...)):
    
    # Processa o texto recebido
    return {"texto_recebido": pesquisa}
