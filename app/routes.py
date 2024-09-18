# from fastapi import APIRouter, Form
# from .YouTubeScraper import YouTubeScraper, robo_get_video_id
# from .main import YouTubeCommentExtractor
# from dotenv import load_dotenv
# import os

# load_dotenv()

# router = APIRouter()
# api_key = os.getenv('API_KEY')
# file_path = os.getenv('FILE_PATH')

# @router.post("/pesquisar")
# async def receber_texto(pesquisa: str = Form(...)):
#     scraper = YouTubeScraper()

#     video_id = robo_get_video_id(pesquisa)

#     extractor = YouTubeCommentExtractor(api_key, video_id)
#     extractor.run(file_path)
#     return {"texto_recebido": pesquisa}
from fastapi import APIRouter, Form
from .YouTubeScraper import YouTubeScraper, robo_get_video_id
from .main import YouTubeCommentExtractor
from .sentiment_analysis import analyze_sentiments
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()
api_key = os.getenv('API_KEY')
file_path = os.getenv('FILE_PATH')

@router.post("/pesquisar")
async def receber_texto(pesquisa: str = Form(...)):

    # Obter o ID do vídeo
    video_id = robo_get_video_id(pesquisa)

    # Extrair comentários do YouTube
    extractor = YouTubeCommentExtractor(api_key, video_id)
    try:
        comments = extractor.run(file_path)  # Certifique-se de que 'run' retorna a lista de comentários
    except Exception as e:
        return {"error": f"Erro ao extrair comentários: {str(e)}"}

    # Certificar-se de que os comentários são uma lista válida
    if not comments or not isinstance(comments, list):
        return {"error": "Nenhum comentário foi extraído ou o formato dos dados está incorreto."}

    # Analisar sentimentos dos comentários
    sentiment_results = analyze_sentiments(comments)

    # Imprimir resultados no console
    for result in sentiment_results:
        print(f"Texto: {result['text']}\nSentimento: {result['sentiment']}, Confiança: {result['confidence']}\n")

    # Retornar os resultados na resposta da API
    return {"pesquisa": pesquisa, "sentimentos": sentiment_results}


