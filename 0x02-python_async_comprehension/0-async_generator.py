#!/usr/bin/env python3
""" coroutines task"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """ wait for randomness"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
