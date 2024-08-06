#!/usr/bin/env python3
"""
Async Comprehension
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A coroutine that will collect 10 random numbers using
    an asynch comprehensing over async_generator

    Returns:
        list of the 10 random numbers
    """
    result = [i async for i in async_generator()]
    return result
