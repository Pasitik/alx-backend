#!/usr/bin/env python3
""" """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ """
    if page < 1 or page_size < 1:
        raise ValueError("page/page size cannot be less than 1")
    start = (page - 1) * page_size
    end = start + page_size
    #end = page * page_size
    #start = end - page_size
    return (start, end)
