#!/usr/bin/python3
"""
This module defines an abstract base class Animal using ABC.
It also provides two concrete subclasses, Dog and Cat,
which implement the abstract method sound().
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    Subclasses must implement the sound() method
    to return the sound specific to that animal.
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Concrete class representing a Dog.

    Attributes:
        _sound: The sound a dog makes (default: "Bark").
    """
    def __init__(self, sound="Bark"):
        self._sound = sound

    def sound(self):
        """return the sound Bark"""
        return self._sound


class Cat(Animal):
    """
    Concrete class representing a Cat.

    Attributes:
        _sound: The sound a cat makes (default: "Meow").
    """
    def __init__(self, sound="Meow"):
        self._sound = sound

    def sound(self):
        """return the sound Meow"""
        return self._sound
