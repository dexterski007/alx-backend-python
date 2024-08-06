#!/usr/bin/env python3
""" coroutines task"""
import asyncio
import random


async def async_generator():
    """ wait for randomness"""
    for i in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
