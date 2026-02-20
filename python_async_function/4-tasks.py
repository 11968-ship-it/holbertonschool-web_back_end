#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that spawns multiple
task_wait_random tasks concurrently and returns their delays
in ascending order without using sort().
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay and
    returns the list of delays in ascending order as they complete.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay in seconds for each task.

    Returns:
        List[float]: A list of delay values in ascending order.
    """
    delays: List[float] = []

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay: float = await task
        delays.append(delay)

    return delays
