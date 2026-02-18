#!/usr/bin/env python3
"""Module that provides a function to zoom a sequence by repeating its
elements.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Return a list where each element of the input tuple is repeated
    'factor' times.
    """
    zoomed_in: List = [item for item in lst for _ in range(factor)]
    return zoomed_in
