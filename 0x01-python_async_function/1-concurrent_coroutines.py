#!/usr/bin/env python3
"""
A module that executes multiple coroutines at the same time with async
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute wait_random n times with a maximum delay of max_delay
    Args:
        n (int): Number of times to execute wait_random
        max_delay (int): Maximum delay for wait_random
    Returns:
        List[float]: List of delays in the order they were completed
    """
    delay_time: List[float] = []
    ordered_list: List[float] = []

    for _ in range(n):
        delay_time.append(wait_random(max_delay))

    for completed_task in asyncio.as_completed(delay_time):
        ordered_list.append(await completed_task)

    return ordered_list
