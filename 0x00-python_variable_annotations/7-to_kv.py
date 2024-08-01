#!/usr/bin/env python3
"""to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string key and the square of a number value.

    Parameters:
    k (str): The key to be included in the tuple.
    v (Union[int, float]): The numerical value to be squared and included
    in the tuple.

    Returns:
    Tuple[str, float]: A tuple where the first element is the key and
    the second element is the square of the value.
    """
    return (k, float(v ** 2))
