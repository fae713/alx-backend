#!/usr/bin/env python3
"""
LFU: Least Frequently Used caching task.
"""
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """
    An LFU caching class.
    """
    def __init__(self):
        super().__init__()
        self.cache_data = {}
        self.freq_map = defaultdict(list)
        self.min_freq = 0

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
            old_freq, _ = self.cache_data[key]
            self.freq_map[old_freq].remove(key)
            if not self.freq_map[old_freq]:
                del self.freq_map[old_freq]
            if old_freq == self.min_freq:
                self.min_freq += 1

        elif len(self.cache_data) >= self.MAX_ITEMS:
            lfu_keys = self.freq_map[self.min_freq]
            if lfu_keys:
                lfu_key = lfu_keys[0]
                self.cache_data.pop(lfu_key)
                self.freq_map[self.cache_data[lfu_key][0]].remove(lfu_key)
                if not self.freq_map[self.cache_data[lfu_key][0]]:
                    del self.freq_map[self.cache_data[lfu_key][0]]
                if self.cache_data[lfu_key][0] == self.min_freq:
                    self.min_freq += 1
                print(f"DISCARD: {lfu_key}")
            else:
                print("Cache is full.")
        else:
            self.min_freq = 1

        self.cache_data[key] = [1, item]

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

        freq, _ = self.cache_data[key]
        self.freq_map[freq].remove(key)
        if not self.freq_map[freq]:
            del self.freq_map[freq]
        if freq == self.min_freq:
            self.min_freq += 1

        self.cache_data[key][0] += 1
        return self.cache_data[key][1]
