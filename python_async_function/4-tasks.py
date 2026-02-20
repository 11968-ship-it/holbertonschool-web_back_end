#!/usr/bin/env python3
"""
Contains a coroutine task_wait_n that spawns task_wait_random
n times with the specified max_delay.
"""
import asyncio
from typing import List

# Dynamic import for the module starting with a digit
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns the list of all the delays (float values).
    
    The list of the delays should be in ascending order without
    using sort() because of the concurrency of as_completed.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Using as_completed to ensure they return in the order they finish
    delays = [await task for task in asyncio.as_completed(tasks)]
    
    return delays
