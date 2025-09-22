#!/usr/bin/python3
"""
This module defines the class BaseGeometry.
"""


class BaseGeometry:
    """
    Class BaseGeometry
    """
    def area(self):
        """
        Raise implementation error if area() is not implemented
        """
        raise NotImplementedError("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value greater than 0 and integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with validated width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Compute and return the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the informal string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square (Rectangle):
    """
    Class Square that inherites from Rectangle
    """
    def __init__(self, size):
        """
        Initialize a Square instance with validated width and height.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
