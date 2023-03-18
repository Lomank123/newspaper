import logging
from typing import List, Dict

import asyncpg
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

    async def _fetch_articles(self) -> Dict:
        """Fetch articles from 3rd party API."""

        async with ClientSession() as client:
            response = await client.get(
                API_URL, params=API_QUERY_STRING, headers=API_HEADERS)
            logger.info(response.status)
            logger.info(type(response.json()))
            return response.json()

    async def _save_articles(self, articles: Dict):
        """Save articles to database."""
        # https://stackoverflow.com/a/43780057/11330677

    async def execute(self):
        # TODO: Handle API errors as well
        articles_data = await self._fetch_articles()
        result = self._save_articles(articles_data)

        return result
