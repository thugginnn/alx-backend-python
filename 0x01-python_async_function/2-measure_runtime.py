#!/usr/bin/env python3
""" Measure the runtime """

from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait
    Args:
        n: number of coroutines to spawn
        max_delay: maximum delay for each coroutine
    Returns: elapsed time in seconds
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n
