#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
from typing import Union


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
