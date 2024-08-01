#!/usr/bin/env python3
""" list of float => sum float """
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """  takes a list input_list of floats as argument
    and returns their sum as a float """
    return float(sum(input_list))
