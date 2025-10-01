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
            raise TypeError("Name is not string")
        if not isinstance(age, int):
            raise TypeError("age is not integer")
        if not isinstance(is_student, bool):
            raise TypeError("is_student is not boolean")

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
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

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
