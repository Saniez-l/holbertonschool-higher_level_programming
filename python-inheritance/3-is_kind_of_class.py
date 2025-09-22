#!/usr/bin/python3
"""
This module defines the function is_kind_of_class
that checks if an object is an instance of a class
or an instance of a subclass of that class.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of the specified class
    or an instance of a subclass of the specified class, otherwise False.

    Args:
        obj: Any Python object.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass,
        otherwise False.
    """
    return type(obj) is a_class or isinstance(obj, a_class)
