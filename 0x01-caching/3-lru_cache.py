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
        self.keys = []

    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data:
                del self.cache_data[self.keys[0]]
                print("DISCARD: {}".format(self.keys[0]))
                del self.keys[0]
            if key in self.keys:
                del self.keys[self.keys.index(key)]

            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data.keys():
            return None
        if key in self.keys:
            del self.keys[self.keys.index(key)]
        self.keys.append(key)
        return self.cache_data[key]
