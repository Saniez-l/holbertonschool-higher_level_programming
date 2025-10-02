#!/usr/bin/python3
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

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Method to print out the object’s attributes with the following format
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

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
        Method to deserialization
        """
        try:
            with open(filename, "rb") as f:
                data = pickle.load(f)
                return data

        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
