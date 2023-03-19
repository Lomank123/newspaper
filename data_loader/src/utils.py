import os
import logging
from faker import Faker
import random

from src.consts import WORD_NUM_FROM, WORD_NUM_TO


fake = Faker()
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


def generate_random_sentence():
    """
    Generate random sentence which contains different amount of words.
    To modify the number of words use `WORD_NUM_FROM` and `WORD_NUM_TO` consts.
    """
    num_of_words = random.randint(WORD_NUM_FROM, WORD_NUM_TO)
    return fake.sentence(nb_words=num_of_words)
