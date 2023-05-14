import asyncio
import logging

import asyncpg
import schema_pb2_grpc as pb2_grpc
from asyncpg import Connection
from grpc import aio
from src.server import ArticleServer
from src.settings import DB_CREDENTIALS, GRPC_PORT

logger = logging.getLogger(__name__)

_cleanup_coroutines = []


async def serve(connection: Connection) -> None:
    """Run the GRPC server."""
    # Async version of GRPC server
    server = aio.server()

    pb2_grpc.add_ArticlesServicer_to_server(ArticleServer(connection), server)
    server.add_insecure_port(f'[::]:{GRPC_PORT}')

    logger.warning('Starting GRPC server...')
    await server.start()

    async def server_graceful_shutdown() -> None:
        logging.warning("Starting graceful shutdown...")
        # Shuts down the server with 5 seconds of grace period. During the
        # grace period, the server won't accept new connections and allow
        # existing RPCs to continue within the grace period.
        await server.stop(5)

    _cleanup_coroutines.append(server_graceful_shutdown())

    await server.wait_for_termination()


async def main() -> None:
    """Entrypoint. Run GRPC server and listen to incoming requests."""
    # Acquire db connection
    connection = await asyncpg.connect(**DB_CREDENTIALS)

    # Run server
    await serve(connection)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        logger.warning('CTRL + C pressed, shutting down the server...')
    finally:
        loop.run_until_complete(*_cleanup_coroutines)
        loop.close()
