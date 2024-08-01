#!/usr/bin/env python3
"""mixed list function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers and floats.

    This function takes a list containing both integers and floats and returns
    the sum of all the elements in the list.

    Parameters:
    mxd_lst (List[Union[int, float]]): The list of integers and/or floats
    to be summed.

    Returns:
    float: The sum of the elements in the list.
    """
    return sum(mxd_lst)
