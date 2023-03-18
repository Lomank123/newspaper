import functools
from typing import Awaitable, Callable

import asyncpg
from asyncpg import Connection
from src.settings import DB_CREDENTIALS


def async_db_connect() -> Callable:
    """Connect to db and pass connection to wrapped function."""
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Awaitable:
            connection: Connection = await asyncpg.connect(**DB_CREDENTIALS)
            try:
                return await func(connection=connection, *args, **kwargs)
            finally:
                await connection.close()
        return wrapped
    return wrapper
