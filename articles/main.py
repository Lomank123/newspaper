import asyncio
import logging

import asyncpg
from src.server import serve
from src.settings import DB_CREDENTIALS

logger = logging.getLogger(__name__)


async def main():
    """Entrypoint. Run GRPC server and listen to incoming requests."""
    # Acquire db connection
    connection = await asyncpg.connect(**DB_CREDENTIALS)

    logger.warning('Starting GRPC server...')
    # Run server
    await serve(connection)


if __name__ == '__main__':
    asyncio.run(main())
