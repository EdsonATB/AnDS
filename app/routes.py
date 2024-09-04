from fastapi import APIRouter, Form
from .YouTubeScraper import YouTubeScraper, robo_get_video_id
from .main import YouTubeCommentExtractor
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()
api_key = os.getenv('API_KEY')
file_path = os.getenv('FILE_PATH')

@router.post("/pesquisar")
async def receber_texto(pesquisa: str = Form(...)):
    scraper = YouTubeScraper()

    video_id = robo_get_video_id(pesquisa)

    extractor = YouTubeCommentExtractor(api_key, video_id)
    extractor.run(file_path)
    return {"texto_recebido": pesquisa}
