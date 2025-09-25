#!/usr/bin/env python3
"""
This modile define class dragon SwimMixin FlyMixin
"""


class SwimMixin:
    """
    Class SwimMixin
    """
    def swim(self):
        """
        define swim
        """
        print("The creature swims!")


class FlyMixin:
    """
    Class FlyMixin
    """
    def fly(self):
        """
        define fly
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class dragon
    """
    def roar(self):
        """
        define roar
        """
        print("The dragon roars!")
