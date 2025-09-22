#!/usr/bin/python3
"""
This module defines the class MyList that inherits list class.
It provides an additional method to print the list elements in sorted order.
"""


class MyList(list):
    """
    A subclass of the built-in list class with an additional method
    to print the list in a sorted (ascending) order.
    """
    def print_sorted(self):
        """
        Print the elements of the list in ascending sorted order.
        """
        print(sorted(self))
