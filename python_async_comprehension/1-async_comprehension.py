#!/usr/bin/env python3
"""
This module imports async_generator and defines async_comprehension.
"""

from typing import List

# Standard way to import based on your project requirements
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    return [i async for i in async_generator()]
