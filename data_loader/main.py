import asyncio
import logging

from src import consts
from src.services import ArticlesLoaderService
from src.settings import API_FETCH_PERIOD_SECS

logger = logging.getLogger(__name__)


async def main():
    """Periodically fetch data from 3rd-party API and save it to DB."""

    logger.info(consts.START_APP_MSG)
    service = ArticlesLoaderService()

    while True:
        try:
            result = await service.execute()
            logger.info(result)
        except Exception as e:
            logger.warning(consts.ERROR_DURING_ITER_MSG)
            logger.error(e)
        finally:
            await asyncio.sleep(API_FETCH_PERIOD_SECS)


if __name__ == '__main__':
    # https://stackoverflow.com/a/73367187/11330677
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info(consts.CLOSE_APP_MSG)
