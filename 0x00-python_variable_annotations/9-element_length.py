#!/usr/bin/env python3
"""Annotate function"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Compute the length of each sequence in an iterable.

    This function takes an iterable of sequences (such as strings,
    lists, or tuples) and returns a list of tuples. Each tuple contains
    a sequence and its length.

    Parameters:
    lst (Iterable[Sequence]): An iterable where each item is a sequence
    (e.g., string, list, tuple).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
    a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
