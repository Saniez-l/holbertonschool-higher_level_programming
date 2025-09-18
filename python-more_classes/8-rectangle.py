#!/usr/bin/python3
"""
this module contain a class rectangle
"""


class Rectangle:
    """
    this class contain class rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        intialisation rectangle witg width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                result += str(self.print_symbol) * self.width + "\n"
        return result.rstrip("\n")

    def __repr__(self):
        """
        return a string representation of the rectangle
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        deleted rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        static method return biggest rectangle based on area
        if equal return rectangle 1
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
