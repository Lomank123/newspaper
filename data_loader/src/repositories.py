import logging
from typing import Dict, List

from asyncpg import Connection, PostgresError
from dateutil import parser
from src import consts
from src.queries import INSERT_ARTICLES_QUERY

logger = logging.getLogger(__name__)


class ArticlesRepository:

    def __init__(self, connection: Connection):
        self.connection = connection

    async def insert_articles(self, articles: List[Dict]) -> Dict:
        # https://stackoverflow.com/a/43780057/11330677
        insert_values = [
            (
                article.get('id'),
                article.get('title'),
                article.get('url'),
                article.get('description'),
                article.get('body'),
                article.get('snippet'),
                article.get('image').get('url'),
                article.get('language'),
                parser.parse(article.get('datePublished')),
            ) for article in articles
        ]
        status = consts.SUCCESS_STATUS
        msg = f"Successfully inserted {len(articles)} item(s)."

        try:
            # executemany returns None if succeeded
            await self.connection.executemany(
                INSERT_ARTICLES_QUERY, insert_values)
        except PostgresError as e:
            # Log error & set msg with status
            logger.warning(consts.ERROR_ON_INSERT_MSG)
            logger.error(e)
            status = consts.ERROR_STATUS
            msg = consts.ERROR_ON_INSERT_MSG
        return {
            "status": status,
            "msg": msg,
        }
