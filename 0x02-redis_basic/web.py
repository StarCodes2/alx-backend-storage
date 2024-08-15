#!/usr/bin/env python3
"""
    Defines a function that uses the requests module to obtain the HTML
    content of a particular URL and returns it, while using a decorator to
    cache the result and track the number of times a particular URL was
    accessed.
"""
import requests
import redis
from functools import wraps
from typing import Callable

red = redis.Redis()


def cache_response(func: Callable) -> Callable:
    """Decorator to cache the result of a function with an expiration time."""
    @wraps(func)
    def wrapper(url: str) -> str:
        result = func(url)
        if result:
            red.setex(url, 10, result)
            red.incr("count:{}".format(url))
        elif not red.exists("count:{}".format(url)):
            red.set("count:{}".format(url), 0)

        return result
    return wrapper


@cache_response
def get_page(url: str) -> str:
    """ Fetch the HTML content of a url and cache it. """
    try:
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException:
        return None
