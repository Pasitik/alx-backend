""" """
#!/usr/bin/env python3


def index_range(page, page_size):
    """ """
    end = page * page_size
    start = end - page_size
    return (start, end)
