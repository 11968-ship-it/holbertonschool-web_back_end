#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that waits for a random
delay between 0 and a specified maximum number of seconds and returns it.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and max_delay
    seconds (inclusive) and returns the delay value.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The randomly generated delay that was awaited.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
