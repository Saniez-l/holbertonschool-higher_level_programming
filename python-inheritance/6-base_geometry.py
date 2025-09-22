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
        raise Exception("area() is not implemented")
