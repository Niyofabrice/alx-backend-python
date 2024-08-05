#!/usr/bin/env python3
"""
A module that measuresthe runtime
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function that measures the total execution time for the wait_n function
    Args:
            n: integer argument
            max_delay: integer argument
    Return:
            Float
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
