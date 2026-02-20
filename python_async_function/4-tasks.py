#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that runs multiple
tasks concurrently using task_wait_random. Each task waits for a
random amount of time up to max_delay seconds. The coroutine collects
all completed delays and returns them in ascending order.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Runs task_wait_random n times concurrently. Each task waits for
    a random delay up to max_delay seconds. As tasks complete, their
    delay values are collected in a list and returned in ascending order.

    Args:
        n (int): The number of tasks to run concurrently.
        max_delay (int): The maximum delay in seconds for each task.

    Returns:
        List[float]: List of float delay values in ascending order.
    """
    tasks: List[asyncio.Task] = [
        task_wait_random(max_delay) for _ in range(n)
    ]

    delays: List[float] = [
        await task for task in asyncio.as_completed(tasks)
    ]

    return delays
