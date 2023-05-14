from pathlib import Path

from dotenv import load_dotenv
from src.utils import get_env_var

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


# GRPC
GRPC_HOST = get_env_var('GRPC_HOST')
GRPC_PORT = get_env_var('GRPC_PORT')

# Logging (unused because FastAPI logging breaks)
# logging.config.fileConfig(os.path.join(BASE_DIR, 'logging.conf'))
