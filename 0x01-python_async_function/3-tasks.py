#!/usr/bin/env python3
"""Tasks"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task to run the `wait_random` coroutine.

    Args:
        max_delay (int): The maximum number of seconds for the `wait_random`
        coroutine.

    Returns:
        asyncio.Task: The `asyncio.Task` object representing the scheduled
        coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
