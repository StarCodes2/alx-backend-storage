#!/usr/bin/env python3
"""
    Defines the Cache class that uses Redis to cache data.
"""
import redis
import uuid
from typing import Union


class Cache():
    """ Using Redis to cache data. """
    def __init__(self):
        """ Init an instance of Cache. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
