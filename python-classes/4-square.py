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
        self.size = size

    @property
    def size(self):
        """retrieve size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area of the square"""
        return self.__size ** 2
