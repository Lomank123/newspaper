import os
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)

# TODO: Move .env and .env.sample files to data_loader dir
DB_CREDENTIALS = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "port": os.environ.get("DB_PORT", "5432"),
    "user": os.environ.get("DB_USER", "db_user"),
    "password": os.environ.get("DB_PASSWORD", "db_pass"),
    "database": os.environ.get("DB_NAME", "db_name"),
}

# API credentials
# TODO: Add a callback which logs if env var is not defined
API_URL = os.environ.get("RAPIDAPI_URL", "https://example.com/")
API_HEADERS = {
    "x-rapidapi-host": os.environ.get("RAPIDAPI_HOST", "host"),
    "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY", "secret_key"),
}

# API search params
PAGE_NUMBER = 1
PAGE_SIZE = 5
AUTO_CORRECT = True
SAFE_SEARCH = False
API_QUERY_STRING = {
    "pageNumber": PAGE_NUMBER,
    "pageSize": PAGE_SIZE,
    "autoCorrect": AUTO_CORRECT,
    "safeSearch": SAFE_SEARCH,
}


FETCH_PERIOD_SECS = 600
