#!/usr/bin/env python3
""" basic async syntax task"""
import asyncio
import random


async def wait_random(max_delay=10):
    """ wait for randomness"""
    waiting = random.uniform(0, max_delay)
    await asyncio.sleep(waiting)
    return waiting
