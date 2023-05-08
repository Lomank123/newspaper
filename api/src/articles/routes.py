from src.articles.services import ArticleService
from fastapi import APIRouter


router = APIRouter()


@router.get('/')
async def articles_list():
    # TODO: Handle case when grpc server is unavailable
    service = ArticleService()
    return await service.get_list()
