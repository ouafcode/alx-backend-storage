#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """ cashe class """
    def __init__(self):
        """ docs method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ doc method """
        keys = str(uuid.uuid4())
        self._redis.set(keys, data)
        return keys

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """ docs method """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """ doc method """
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """ doc method """
        return self.get(key, fn=int)
