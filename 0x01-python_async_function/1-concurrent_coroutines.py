#!/usr/bin/env python3
"""multiple coroutines at the same time with async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn multiple coroutines that wait for a random delay and return
    a list of delays.

    Args:
        n (int): The number of `wait_random` coroutines to spawn.
        max_delay (int): The maximum number of seconds to wait for each
        coroutine.

    Returns:
        List[float]: A list of random delays for each coroutine.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    list_delay = await asyncio.gather(*tasks)
    return list_delay
