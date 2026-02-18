#!/usr/bin/env python3
"""Module that provides a function to zoom a sequence by repeating its elements."""

from typing import Tuple, List, TypeVar

T = TypeVar('T')


def zoom_array(lst: Tuple[T, ...], factor: int = 2) -> List[T]:
    """
    Return a list where each element of the input tuple is repeated 'factor' times.
    """
    zoomed_in: List[T] = [item for item in lst for _ in range(factor)]
    return zoomed_in


# Example usage
array: Tuple[int, ...] = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
