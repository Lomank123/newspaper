import logging.config
import os
from pathlib import Path

from dotenv import load_dotenv
from src.utils import get_env_var

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent

# DB settings

DB_CREDENTIALS = {
    "host": get_env_var("DB_HOST", "localhost"),
    "port": get_env_var("DB_PORT", "5432"),
    "user": get_env_var("DB_USER", "db_user"),
    "password": get_env_var("DB_PASSWORD", "db_pass"),
    "database": get_env_var("DB_NAME", "db_name"),
}


# API settings

API_URL = get_env_var("RAPIDAPI_URL", "https://example.com/")
API_HEADERS = {
    "x-rapidapi-host": get_env_var("RAPIDAPI_HOST", "host"),
    "x-rapidapi-key": get_env_var("RAPIDAPI_KEY", "secret_key"),
}

API_FETCH_PERIOD_SECS = 600

# Search params
PAGE_NUMBER = 1
PAGE_SIZE = 20
# Bool variables won't work, so pass them as strings
# https://github.com/aio-libs/aiohttp/issues/4874
AUTO_CORRECT = "true"
SAFE_SEARCH = "false"
API_QUERY_STRING = {
    # "q": "taylor swift",      # For tests
    "pageNumber": PAGE_NUMBER,
    "pageSize": PAGE_SIZE,
    "autoCorrect": AUTO_CORRECT,
    "safeSearch": SAFE_SEARCH,
}


# Logging

logging.config.fileConfig(os.path.join(BASE_DIR, 'logging.conf'))
