import os
import logging


logger = logging.getLogger(__name__)


def get_env_var(key, default=None):
    """
    Return env variable value if it was found by `key`.
    Otherwise log the fact that var was not found and return `default`.
    """
    env_val = os.environ.get(key)

    if env_val is None:
        msg = f"{key} was not found in .env file. Default value is '{default}'"
        if not default:
            msg += 'empty.'
        logger.warning(msg)
        return default

    return env_val
