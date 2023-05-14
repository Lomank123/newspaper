import logging

import schema_pb2 as pb2
import schema_pb2_grpc as pb2_grpc
from asyncpg import Connection

logger = logging.getLogger(__name__)


class ArticleServer(pb2_grpc.ArticlesServicer):
    """GRPC Server."""

    def __init__(self, connection: Connection):
        super().__init__()
        self.connection = connection

    # TODO: Google what types does this args have
    async def ArticleListResponse(self, request, context) -> pb2.ArticleList:
        query = 'SELECT * FROM articles ORDER BY id ASC LIMIT 10;'
        result = await self.connection.fetch(query=query)
        articles = [
            pb2.Article(
                id=row.get('id'),
                api_id=row.get('api_id'),
                title=row.get('title'),
                url=row.get('url'),
                description=row.get('description'),
                body=row.get('body'),
                snippet=row.get('snippet'),
                img_url=row.get('img_url'),
                language=row.get('language'),
                published_at=str(row.get('published_at')),
            ) for row in result
        ]
        return pb2.ArticleList(article=articles)
