from src.articles.services import CreateArticleService, GetArticleService
from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def articles_list():
    service = GetArticleService()
    data = service.get_list()
    return data


@router.get('/{id}')
async def article_by_id(id: int):
    service = GetArticleService()
    data = service.filter_by()
    return data


@router.post('/')
async def create_article():
    service = CreateArticleService()
    data = service.create()
    return data
