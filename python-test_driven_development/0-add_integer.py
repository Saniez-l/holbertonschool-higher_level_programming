#!/usr/bin/python3
"""
Module 0-add_integer
contain fonction 
add_integer add two integer.
"""


def add_integer(a, b=98):
    """
    add two integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
