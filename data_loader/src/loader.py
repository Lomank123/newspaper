import logging
from typing import List, Dict
from dateutil import parser

from aiohttp import ClientSession
from asyncpg import Connection
from src.queries import INSERT_ARTICLES_QUERY
from src.settings import API_URL, API_QUERY_STRING, API_HEADERS

logger = logging.getLogger(__name__)


class ArticlesLoaderService:
    """
    Fetch articles from 3rd-party API and save them to the database.
    """

    def __init__(self, connection: Connection):
        self.connection = connection

    async def _fetch_articles(self) -> List[Dict]:
        """Fetch articles from 3rd party API."""

        async with ClientSession() as client:
            response = await client.get(
                API_URL, params=API_QUERY_STRING, headers=API_HEADERS)
            articles_data = await response.json()
            return articles_data.get('value')

    async def _save_articles(self, articles: List[Dict]):
        """Save articles to database."""
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
        # TODO: Logs should appear in the console upon execution, add logs
        # TODO: try except here
        # https://magicstack.github.io/asyncpg/current/api/index.html#asyncpg.connection.Connection.executemany
        # executemany returns None if succeeded, so we should check errors
        return await self.connection.executemany(
            INSERT_ARTICLES_QUERY, insert_values)

    async def execute(self):
        # TODO: Handle API errors as well
        articles_data = await self._fetch_articles()
        result = await self._save_articles(articles_data)

        return result
