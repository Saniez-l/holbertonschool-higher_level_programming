#!/usr/bin/python3
"""
This module contain a class Square
"""


class Square:
    """
    this class contain class Square
    """
    def __init__(self, size=0):
        """
        intitialisation square with size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
