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
    Executes task_wait_random n times with the given max_delay
    and returns the delays in ascending order as tasks complete.
    """
    delays: List[float] = []

    tasks: List[asyncio.Task] = [
        task_wait_random(max_delay) for _ in range(n)
    ]

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
