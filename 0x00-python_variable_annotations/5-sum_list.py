#!/usr/bin/env python3
import typing
""" list of float => sum float """


def sum_list(input_list: typing.List[float]) -> float:
    """  takes a list input_list of floats as argument
    and returns their sum as a float """
    return float(sum(input_list))
