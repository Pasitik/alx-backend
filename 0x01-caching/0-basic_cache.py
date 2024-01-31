#!/usr/bin/python3
""" BaseCaching module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        Defines a class for caching information in key-value pairs
    """
    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
