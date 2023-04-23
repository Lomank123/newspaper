import logging.config
import os
from pathlib import Path

from dotenv import load_dotenv
# from src.utils import get_env_var

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent

# Logging

logging.config.fileConfig(os.path.join(BASE_DIR, 'logging.conf'))
