#!/usr/bin/env python3
"""make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    This function returns a new function that multiplies its input
    by a specified multiplier.

    Parameters:
    multiplier (float): The value by which the input of the returned function
    will be multiplied.

    Returns:
    Callable[[float], float]: A function that takes a float as input
    and returns the product of that input and the specified multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
