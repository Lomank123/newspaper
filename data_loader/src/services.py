import logging
from typing import Dict, List

from aiohttp import ClientSession
from asyncpg import Connection
from src.decorators import async_db_connect
from src.repositories import ArticlesRepository
from src.settings import API_HEADERS, API_QUERY_STRING, API_URL
from src.utils import generate_random_sentence
from src import consts

logger = logging.getLogger(__name__)


class ArticlesLoaderService:
    """
    Fetch articles from 3rd-party API and save them to the database.
    """

    async def _fetch_articles(self) -> List[Dict]:
        """Fetch articles from 3rd party API."""

        async with ClientSession() as client:
            params = {
                "q": generate_random_sentence(),
                **API_QUERY_STRING,
            }
            try:
                response = await client.get(
                    API_URL, params=params, headers=API_HEADERS)
                # TODO: Output only necessary data here
                logger.info(params)
                logger.info(f"Response status: {response.status}")
                articles_data = await response.json()
                return articles_data.get('value', list())
            except Exception as e:
                logger.warning(consts.ERROR_ON_DATA_FETCH_MSG)
                logger.error(e)
                return list()

    @async_db_connect()
    async def execute(self, connection: Connection):
        articles_data = await self._fetch_articles()
        # articles_data = list()
        repository = ArticlesRepository(connection)
        return await repository.insert_articles(articles_data)
