#!/usr/bin/env python3
""" list of mixed => sum float """
from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """ takes a string k and an int OR
    float v as arguments and returns a tuple """
    new_tuple = (k, float(v ** 2))
    return new_tuple
