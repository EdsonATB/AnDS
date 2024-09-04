from fastapi import APIRouter, Form
from .YouTubeScraper import YouTubeScraper, robo_get_video_id
from .main import YouTubeCommentExtractor


router = APIRouter()
api_key = ''
file_path = ''

@router.post("/pesquisar")
async def receber_texto(pesquisa: str = Form(...)):
    scraper = YouTubeScraper()

    video_id = robo_get_video_id(pesquisa)

    extractor = YouTubeCommentExtractor(api_key, video_id)
    extractor.run(file_path)
    return {"texto_recebido": pesquisa}
