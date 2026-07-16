import json
import os

import redis
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Redis URL
REDIS_URL = os.getenv("REDIS_URL")

if REDIS_URL is None:
    raise ValueError("REDIS_URL environment variable is not set.")

# Create Redis client
redis_client = redis.StrictRedis.from_url(
    REDIS_URL,
    decode_responses=True,
)


def get_cached_prediction(key: str) -> dict | None:
    """
    Retrieve a cached prediction from Redis.

    Args:
        key: Cache key.

    Returns:
        Cached dictionary if found, otherwise None.
    """
    value = redis_client.get(key)

    if value is None:
        return None

    return json.loads(value)


def set_cached_prediction(key: str, value: dict) -> None:
    """
    Store a prediction in Redis.

    Args:
        key: Cache key.
        value: Prediction dictionary.
    """
    redis_client.set(
        key,
        json.dumps(value),
    )
