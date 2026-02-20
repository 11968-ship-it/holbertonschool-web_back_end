#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that executes multiple
tasks concurrently using task_wait_random and returns their delays
in ascending order as the tasks complete.
"""

import asyncio
from typing import List

# Ensure this import matches your file structure exactly
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.
    
    Args:
        n (int): number of times to spawn the task
        max_delay (int): maximum delay for each task
        
    Returns:
        List[float]: list of delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Using as_completed to ensure they return in finished order (ascending)
    delays = [await task for task in asyncio.as_completed(tasks)]
    
    return delays
