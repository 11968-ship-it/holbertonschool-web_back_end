#!/usr/bin/env python3
"""
Task 4's module to spawn Tasks using task_wait_random.
"""
import asyncio
from typing import List

# Explicitly importing the task-based function
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: The list of all the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Using as_completed ensures the results are returned in the order 
    # they finish (ascending), which satisfies the 'no sort()' requirement.
    delays = [await task for task in asyncio.as_completed(tasks)]
    
    return delays
