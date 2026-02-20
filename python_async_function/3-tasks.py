#!/usr/bin/env python3
"""
This module defines a function that creates and returns an asyncio.Task
for the wait_random coroutine.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that executes the
    wait_random coroutine with the specified max_delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The created task object.
    """
    return asyncio.create_task(wait_random(max_delay))
