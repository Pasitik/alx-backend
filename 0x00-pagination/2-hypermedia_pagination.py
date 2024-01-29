#!/usr/bin/env python3
"""
Defines class Server that paginates a database of popular baby names
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ """
    end = page * page_size
    start = end - page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        dataset = self.dataset()
        index = index_range(page, page_size)
        return dataset[index[0]:index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ """
        dataset = self.dataset()
        total_pages = len(dataset) // page_size + 1
        data = self.get_page(page, page_size)
        page_size = len(data)
        if page >= total_pages:
            next_page = None
        else:
            next_page = page + 1
        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1
        return {"page_size": page_size,
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages}
