from data_loader.decorators import async_db_connect
import asyncpg
import asyncio
import logging
from data_loader.settings import FETCH_PERIOD_SECS

logger = logging.getLogger(__name__)


# TODO: Use typehints
async def fetch_articles():
    """Fetch articles from 3rd party API."""
    # TODO: Use aiohttp to get data
    pass


@async_db_connect()
async def main(connection):
    # TODO: Handle API errors as well
    while True:
        articles = await fetch_articles()
        logger.info(articles)
        await asyncio.sleep(FETCH_PERIOD_SECS)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    try:
        loop.run_until_complete(task)
    except asyncio.CancelledError as e:
        logger.info(str(e))
