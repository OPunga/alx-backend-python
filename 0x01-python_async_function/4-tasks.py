#!/usr/bin/env python3
"""python and async coroutines"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return list with all delayed tasks"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delayed_tasks = [await task for task in asyncio.as_completed(tasks)]
    return delayed_tasks
