#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that spawns multiple
task_wait_random tasks concurrently and returns their delays
in ascending order without using sort().
"""
import asyncio
from typing import List

# Import task_wait_random from the previous task file
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.
    
    Returns:
        List[float]: A list of all the delays (float values) in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # as_completed yields tasks as they finish, regardless of order started
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
        
    return delays
