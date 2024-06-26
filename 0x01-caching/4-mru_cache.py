#!/usr/bin/env python3
"""
MRU: Most Recently Used caching task.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    An MRU caching class.
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache with a key and value.

        Args:
            key: The key of the item.
            item: The value stored in the key.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = next(reversed(self.cache_data))
            self.cache_data.pop(mru_key)
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the key:value pair in the cache.

        Args:
            key: The key to retrieve.

        Returns:
            The key:value or None if the key does not exist.
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed item to the end to mark it as most recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
