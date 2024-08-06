#!/usr/bin/env python3
"""
Async generator
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    A coroutine function that loops 10 times, each time asynchronously
    wait 1 second, and then yield a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
