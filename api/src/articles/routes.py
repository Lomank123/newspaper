from src.articles.services import ArticleService
from fastapi import APIRouter


router = APIRouter()


@router.get('/')
async def articles_list():
    # TODO: Handle case when grpc server is unavailable
    service = ArticleService()
    data = service.get_list()
    return data
