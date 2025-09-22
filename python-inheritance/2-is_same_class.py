#!/usr/bin/python3
"""
This module defines the function is_same_class
that checks if an object is exactly an instance
of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Return True if the object is exactly an instance
    of the specified class, otherwise False.

    Args:
        obj: Any Python object.
        a_class: The class to compare the type of obj against.

    Returns:
        bool: True if obj is an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
