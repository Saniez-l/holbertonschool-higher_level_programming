#!/usr/bin/env python3
"""
Pickling Custom Classes
"""
import pickle


class CustomObject:
    """
    Class customobject
    """

    def __init__(self, name, age, is_student):
        """
        Init name, age, is_student
        """
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(age, int):
            raise TypeError
        if not isinstance(is_student, bool):
            raise TypeError

        self.Name = name
        self.Age = age
        self.Is_student = is_student

    def display(self):
        """
        Method to print out the object’s attributes with the following format
        """
        print(f"Name: {self.Name}")
        print(f"Age: {self.Age}")
        print(f"Is Student: {self.Is_student}")

    def serialize(self, filename):
        """
        Method to serialisation with pickle
        """
        if filename is None:
            return None
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Method to deserialisation
        """
        try:
            with open(filename, "rb") as f:
                data = pickle.load(f)
            return data

        except (FileNotFoundError, pickle.UnpicklingError):
            return None
