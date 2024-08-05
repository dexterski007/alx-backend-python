#!/usr/bin/env python3
""" execute multiple coroutines at the same time with async """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ wait for randomness"""
    delays = []
    for _ in range(n):
        delay = task_wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)
