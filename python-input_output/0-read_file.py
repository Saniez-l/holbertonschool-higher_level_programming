#!/usr/bin/python3
"""
Module for read file
"""


def read_file(filename=""):
    """
    Read file with open and encodings UTF8
    """

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
    f.close
