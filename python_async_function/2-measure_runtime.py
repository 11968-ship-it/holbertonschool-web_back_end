#!/usr/bin/env python3
"""
This module defines a function that measures the average execution
time of running the wait_n coroutine.
"""

import asyncio
import time
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time of wait_n with the given
    arguments and returns the average time per coroutine.

    Args:
        n (int): The number of times wait_random is spawned.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average execution time per coroutine.
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()

    total_time: float = end_time - start_time
    return total_time / n
