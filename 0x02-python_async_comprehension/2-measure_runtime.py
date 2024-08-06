#!/usr/bin/env python3
"""four parallel comprehensions"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Asynchronous function that measures the time taken to execute four
    instances of async_comprehension in parallel.

    Returns:
        float: The total time taken to execute the four comprehensions.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return (end_time - start_time)
