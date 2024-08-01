#!/usr/bin/env python3
""" typevar exercise """
from typing import Tuple, List, Any, Iterable


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ fixing  """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple[Any, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
