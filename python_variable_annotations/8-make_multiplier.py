#!/usr/bin/env python3
"""Module that provides a function to create a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.
    """
    def multiplier_func(n: float) -> float:
        """Multiply the input float by the multiplier and return the result."""
        return n * multiplier

    return multiplier_func
