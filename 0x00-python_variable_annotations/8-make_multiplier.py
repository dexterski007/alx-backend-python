#!/usr/bin/env python3
""" takes a float multiplier as argument """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """  takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier """
    def fmultiplier(val: float) -> float:
        """ subfunction to multiply float """
        return val * multiplier
    return fmultiplier
