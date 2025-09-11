#!/usr/bin/python3
"""
This module has a function that prints a square using the character #
"""


def print_square(size):
    """
    Prints a square of size `size` using the character #

    Args:
        size (int): length of the square sides

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is < 0

    Examples:
    >>> print_square(3)
    ###
    ###
    ###
    >>> print_square(1)
    #
    >>> print_square(0)
    <BLANKLINE>
    >>> print_square(-1)
    Traceback (most recent call last):
        ...
    ValueError: size must be >= 0
    >>> print_square(3.5)
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer
    """
    # check type
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # check value
    if size < 0:
        raise ValueError("size must be >= 0")

    # chexk equalzero
    if size == 0:
        print()
        return

    # print square
    for i in range(size):
        print("#" * size)
