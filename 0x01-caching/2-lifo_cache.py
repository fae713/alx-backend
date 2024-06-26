#!/usr/bin/env python3
"""
LIFO: Last In, First Out caching task.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    A LIFO caching class.
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        This adds an item to the dict with a key and value.

        args:
            key -> the key of the item.
            item -> the value stored in the key.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)

        elif len(self.cache_data) >= self.MAX_ITEMS:
            last_key = next(reversed(self.cache_data))
            self.cache_data.pop(last_key)
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        This gets the key:value pair in the dict.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key, None)
