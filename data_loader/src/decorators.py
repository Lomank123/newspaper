import functools
import asyncpg
from data_loader.settings import DB_CREDENTIALS


# TODO: Use typehints
def async_db_connect():
    """Connect to db and pass connection to wrapped function."""
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            connection = await asyncpg.connect(**DB_CREDENTIALS)
            try:
                return await func(connection=connection, *args, **kwargs)
            finally:
                await connection.close()
        return wrapped
    return wrapper
