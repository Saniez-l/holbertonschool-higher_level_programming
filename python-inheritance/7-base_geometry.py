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
