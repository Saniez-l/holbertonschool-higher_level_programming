#!/usr/bin/python3
"""
This module has a function that prints a text
with 1 new line after '.', '?' and ':'
"""


def text_indentation(text):
    """
    Prints a text with 1 new line after '.', '?' or ':'

    Args:
        text (str): the text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    end_chars = ['.', '?', ':']
    start = 0
    length = len(text)

    for i, char in enumerate(text):
        if char in end_chars:
            line = text[start:i + 1].strip()
            print(line)
            # Only print newline if this is NOT the last character of the text
            if i + 1 < length:
                print()
            start = i + 1
