#!/usr/bin/env python3
""" task 2 of coroutines """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_generator


async def measure_runtime() -> float:
    """ async comprehensions """
    begin = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return begin - end
