#!/usr/bin/python3
"""
    Least Recently used
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
        LRU
    """
    def __init__(self):
        super().__init__()
        self.keys_list = []

    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data:
                del self.cache_data[self.keys_list[0]]
                print("DISCARD: {}".format(self.keys_list[0]))
                del self.keys_list[0]
            if key in self.keys_list:
                del self.keys_list[self.keys_list.index(key)]

            self.cache_data[key] = item
            self.keys_list.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data.keys():
            return None
        if key in self.keys_list:
            del self.keys_list[self.keys_list.index(key)]
        self.keys_list.append(key)
        return self.cache_data[key]
