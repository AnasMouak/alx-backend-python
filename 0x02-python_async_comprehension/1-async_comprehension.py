#!/usr/bin/env python3
"""Async Comprehensions"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous function that collects values from async_generator into a list

    Returns:
        list of float: A list containing 10 random floating-point numbers
        collected from async_generator.
    """
    result = [value async for value in async_generator()]
    return result
