#!/usr/bin/env python3
"""Run time for four parallel comprehensions module"""


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run time for four parallel comprehensions"""

    start = time.time()
    tasks = [async_comprehension() for x in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    time_taken = end - start

    return time_taken
