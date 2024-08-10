#!/usr/bin/env python3
"""
Complex types - mixed list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function that takes a list of integers and floats and return their sum
    """
    return sum(mxd_lst)
