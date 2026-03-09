#!/usr/bin/env python3
"""Module that provides a helper function for pagination."""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple containing the start and end index for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: The start index and end index corresponding
        to the items to be returned for the given page.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
