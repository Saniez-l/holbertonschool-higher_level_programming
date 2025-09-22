#!/usr/bin/python3
"""
This module defines the function inherits_from
that checks if an object is an instance of a subclass
(inherited directly or indirectly) of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Return True if the object is an instance of a subclass of the given class,
    otherwise False. An object that is exactly an instance of a_class
    should return False.

    Args:
        obj: Any Python object.
        a_class: The class to check inheritance against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
        otherwise False.
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
