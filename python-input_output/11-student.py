#!/usr/bin/python3
"""
class student return dictionnary representation of
a student instance only attribute names
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

    def to_json(self, attrs=None):
        """
        Dictionary representation of a Student instance only attribute names
        """
        if isinstance(attrs, list) and all(isinstance(item, str)
                                           for item in attrs):
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}

        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
