#!/usr/bin/env python3
"""
    Defines the Cache class that uses Redis to cache data.
"""
import redis
import uuid
from typing import Callable, Optional, Union


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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes,
                                                                    int,
                                                                    float]:
        """ Returns a value in a specific data format. """
        data = self._redis.get(key)
        if data is None:
            return None

        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """ Return a value in string format. """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[str]:
        """ Return a value in int format. """
        return sefl.get(key, fn=int)
