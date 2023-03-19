import logging
import asyncio

from asyncpg import Connection
from src.decorators import async_db_connect
from src.loader import ArticlesLoaderService

from src.settings import API_FETCH_PERIOD_SECS


logger = logging.getLogger(__name__)


@async_db_connect()
async def main(connection: Connection):
    """Periodically fetch data from 3rd-party API and save it to DB."""
    service = ArticlesLoaderService(connection)
    # TODO: Add logs when the script starts, ends or throws error
    while True:
        result = await service.execute()
        logger.info(result)
        await asyncio.sleep(API_FETCH_PERIOD_SECS)


if __name__ == '__main__':
    # Deprecated
    # Check out this: https://stackoverflow.com/a/73367187/11330677
    # loop = asyncio.get_event_loop()
    # task = loop.create_task(check_pg_version())
    # loop.run_until_complete(task)

    asyncio.run(main())
