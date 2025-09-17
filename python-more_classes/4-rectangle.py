#!/usr/bin/python3
"""
this module contain a class rectangle
"""


class Rectangle:
    """
    this class contain class rectangle
    """
    def __init__(self, width=0, height=0):
        """
        intialisation rectangle witg width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter to retrieve width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width with validation
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter to retrieve height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height with validation
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        return area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        return perimetre
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """
        print # for rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            result = ""
            for _ in range(self.height):
                result += "#" * self.width + "\n"
        return result.rstrip("\n")

    def __repr__(self):
        """
        return a string representation of the rectangle
        """
        return f"Rectangle ({self.width}, {self.height})"
