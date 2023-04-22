from fastapi import FastAPI
from src.services import CreateArticleService, GetArticleService

app = FastAPI()


@app.get("/")
async def articles_list():
    service = GetArticleService()
    data = service.get_list()
    return data


@app.get('/{id}')
async def article_by_id(id: int):
    service = GetArticleService()
    data = service.filter_by()
    return data


@app.post("/")
async def create_article():
    service = CreateArticleService()
    data = service.create()
    return data
