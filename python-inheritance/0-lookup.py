#!/usr/bin/python3
"""
This module provides the function `lookup`
that returns the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of the given object.

    Args:
        obj: Any Python object.

    Returns:
        list: A list of attribute and method names.
    """
    return dir(obj)
