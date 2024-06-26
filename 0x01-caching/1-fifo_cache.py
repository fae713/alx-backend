#!/usr/bin/env python3
"""
FIFO: First In, First Out task.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    A caching system class.
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
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        This gets the key:value pair in the dict.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
