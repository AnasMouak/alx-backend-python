#!/usr/bin/env python3
"""The basics of async"""
import random
import asyncio


async def wait_random(max_delay=10):
    """
    Asynchronously wait for a random delay and return a random float.

    Args:
        max_delay (int, optional): The maximum number of seconds to wait.
                                   Defaults to 10.

    Returns:
        float: A random float between 0 and `max_delay`.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
