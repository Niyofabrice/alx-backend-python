#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A coroutine that measures the total runtime of 4
    parallel async_comprehension using asyncio.gather

    Returns:
        total runtime
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start_time
    return total_time
