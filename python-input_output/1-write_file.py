#!/usr/bin/python3
"""
Module for write file and return number of caractere
"""


def write_file(filename="", text=""):
    """
    function write and return caractere with utf8
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
