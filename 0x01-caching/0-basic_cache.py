#!/usr/bin/env python3
"""
Basic Dictionary task.
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    This class creates a basic dictionary.
    """
    def put(self, key, item):
        """
        This adds an item to the dict with a key and value.

        args: 
            key -> the key of the item.
            item -> the value stored in the key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
    
    def get(self, key):
        """
        This gets the key:value pair in the dict.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)


