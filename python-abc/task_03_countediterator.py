#!/usr/bin/python3
"""
This module CountedIterator
"""


class CountedIterator:
    """
    Class CountedIterator
    """

    def __init__(self, iterable, counter=0):
        """
        Define iterable and counter
        """
        self.__iterator = iter(iterable)
        self.__counter = counter

    def __iter__(self):
        """
        Define __iter__
        Return self
        """
        return self

    def get_count(self):
        """
        Define get_count
        Return self.__counter
        """
        return self.__counter

    def __next__(self):
        """
        Define __next__ for change iterator
        return valeur
        """
        valeur = next(self.__iterator)
        self.__counter += 1
        return valeur
