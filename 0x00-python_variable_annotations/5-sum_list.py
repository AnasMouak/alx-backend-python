#!/usr/bin/env python3
"""sum_list function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    This function takes a list of float numbers and returns their sum.

    Parameters:
    input_list (List[float]): The list of floats to be summed.

    Returns:
    float: The sum of the floats in the list.
    """
    return sum(input_list)
