#!/usr/bin/python3
"""
    Last in, First out
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        LIFO
    """
    def __init__(self):
        """class initialization"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """updates cache"""
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data:
                del self.cache_data[self.keys[-1]]
                print("DISCARD: {}".format(self.keys[-1]))
                del self.keys[-1]
            if key in self.keys:
                del self.keys[self.keys.index(key)]

            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """retrieves item from cache"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
