#!/usr/bin/python3
"""
Module write with apend and return len text
"""


def append_write(filename="", text=""):
    """
    Append text with encoding utf-8 and return len of text
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
