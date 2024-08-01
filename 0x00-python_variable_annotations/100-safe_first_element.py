#!/usr/bin/env python3
""" dukctype iterable """
from typing import Optional, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """ function to fix """
    if lst:
        return lst[0]
    else:
        return None
