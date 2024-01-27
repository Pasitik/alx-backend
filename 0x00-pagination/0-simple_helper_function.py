#!/usr/bin/env python3
""" """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ """
    if page < 1 or page_size < 1:
        raise "page/page size cannot be less than 1"
    end = page * page_size
    start = end - page_size
    return (start, end)
