#!/usr/bin/env python3
""" """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ """
    end = page * page_size
    start = end - page_size
    return (start, end)
