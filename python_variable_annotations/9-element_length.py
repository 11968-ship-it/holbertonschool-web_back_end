#!/usr/bin/env python3
"""Module that provides a function to return elements and their lengths."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples, each containing an element from the input
    and its length.
    """
    return [(i, len(i)) for i in lst]
