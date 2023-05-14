import logging

from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
from src.articles.services import ArticleService

logger = logging.getLogger(__name__)


router = APIRouter()


@router.get('/')
async def articles_list() -> Response:
    service = ArticleService()
    articles_list = await service.get_list()

    # Close GRPC channel gracefully
    await service.close_channel()

    return JSONResponse(content=articles_list)
