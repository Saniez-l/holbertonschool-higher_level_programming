#!/usr/bin/python3
"""
This module defines the BaseGeometry class, which serves as a base
class for geometry-related operations. It provides a validation
method and an abstract area method.
"""


class BaseGeometry:
    """
    BaseGeometry class that serves as an interface for geometry operations.
    Provides validation and an abstract method area().
    """
    def area(self):
        """
        Public instance method that raises an Exception
        indicating that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that 'value' is a positive integer.
        Raises TypeError if value is not an integer,
        and ValueError if value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
