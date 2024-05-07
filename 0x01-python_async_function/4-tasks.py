#!/usr/bin/env python3
"" Task 4 Module """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with a specified delay
    between each call.
    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay for each coroutine
    Returns:
        list of all delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
