#!/usr/bin/python3
"""
Module 0-add_integer
contain fonction add_integer add two integer.
"""

def add_integer(a, b=98):
    """
    add two integer or float.

    Args:
        a (int ou float): first number
        b (int ou float, optionnel): second number by default (98)

    Returns:
        int: sum of two number 

    Exceptions:
        TypeError: if a or b is not integer or gloat
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)