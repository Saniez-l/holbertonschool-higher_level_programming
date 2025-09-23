#!/usr/bin/python3
"""
This module defines an abstract base class
Shape and its concrete subclasses Circle and Rectangle.
It also provides a function shape_info to display the
area and perimeter of any shape.
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.

    Subclasses must implement the area() and perimeter() methods.
    """
    @abstractmethod
    def area(self):
        """
        Compute and return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Compute and return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Concrete class representing a circle.

    Attributes:
        radius (float): The radius of the circle.
    """
    def __init__(self, radius):
        """
        Initialize a Circle with a given radius.
        """
        self.radius = radius

    def area(self):
        """
        Return the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Return the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a rectangle.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle with given width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Display the area and perimeter of a given shape.
    """
    print("Area: ", shape.area())
    print("Perimeter: ", shape.perimeter())
