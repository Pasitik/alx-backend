"""
    First in, First out
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        FIFO
    """
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            self.keys.append(key)

        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.keys[0]]
            print("DISCARD: {}".format(self.keys[0]))
            del self.keys[0]

    def get(self, key):
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
