#!/usr/bin/env python3
"""Basic caching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    an object that allows storting of data and retrivalof data
    """
    def put(self, key, item):
        """
        put function adds item
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
