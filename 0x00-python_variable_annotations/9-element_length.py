#!/usr/bin/env python3
""" dukctype iterable """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """  function to fix """
    return [(i, len(i)) for i in lst]
