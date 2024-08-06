#!/usr/bin/env python3
""" coroutines task"""
from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """ wait for randomness"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
