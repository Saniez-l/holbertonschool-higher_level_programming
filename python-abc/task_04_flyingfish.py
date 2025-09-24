#!/usr/bin/python3
"""
This module Exploring Multiple Inheritance
"""


class Fish:
    """
    Class Fish
    """
    pass

    def swim(self):
        """
        Print method
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print method
        """
        print("The fish lives in water")


class Bird:
    """
    Class Bird
    """
    pass

    def fly(self):
        """
        Print method
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print method
        """
        print("The bird lives in the sky")


class FlyingFish(Bird, Fish):
    """
    Class FlyingFish
    """

    def fly(self):
        """
        Print method
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Print method
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Print method
        """
        print("The flying fish lives both in water and the sky!")
