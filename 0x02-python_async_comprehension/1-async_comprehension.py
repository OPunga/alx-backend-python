#!/usr/bin/env python3
"""Async comprehensions module"""


import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """An asynchronous comprehensions function"""

    async_list = [i async for i in async_generator()]

    return async_list
