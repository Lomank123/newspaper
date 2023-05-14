import logging.config
import os
from pathlib import Path

from dotenv import load_dotenv
from src.utils import get_env_var

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent

# GRPC

GRPC_PORT = get_env_var('GRPC_PORT')


# Articles DB

DB_CREDENTIALS = {
    "host": get_env_var("DB_HOST", "localhost"),
    "port": get_env_var("DB_PORT", "5432"),
    "user": get_env_var("DB_USER", "db_user"),
    "password": get_env_var("DB_PASSWORD", "db_pass"),
    "database": get_env_var("DB_NAME", "db_name"),
}


# Logging

logging.config.fileConfig(os.path.join(BASE_DIR, 'logging.conf'))
