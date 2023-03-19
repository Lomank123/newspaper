import logging
from typing import Dict, List

from asyncpg import Connection, PostgresError
from dateutil import parser
from src.queries import INSERT_ARTICLES_QUERY
from src import consts


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

        # https://magicstack.github.io/asyncpg/current/api/index.html#asyncpg.connection.Connection.executemany
        # executemany returns None if succeeded

        # TODO: Perhaps there should be Parent class with similar error handling logic
        try:
            await self.connection.executemany(
                INSERT_ARTICLES_QUERY, insert_values)
        except PostgresError as e:
            logger.warning(consts.ERROR_ON_INSERT_MSG)
            logger.error(e)
            status = consts.ERROR_STATUS
            msg = consts.ERROR_ON_INSERT_MSG
        return {
            "status": status,
            "msg": msg,
        }
