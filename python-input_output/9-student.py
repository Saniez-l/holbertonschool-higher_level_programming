#!/usr/bin/python3
"""
class student return dictionnary representation of a student instance
"""


class Student:
    """
    Write a class Student that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialisation class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Dictionary representation of a Student instance
        """
        return self.__dict__
