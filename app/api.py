from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes import router

app = FastAPI()

app.include_router(router)


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_index():
    return FileResponse("static/index.html")


#Para iniciar a api abra o terminal e digite uvicorn app.main:app --reload
#Para iniciar a api abra o terminal e digite uvicorn app.api:app --reload