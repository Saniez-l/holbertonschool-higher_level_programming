#!/usr/bin/python3
"""
Module for read file
"""

def read_file(filename=""):
    """
    Read file with open and encodings UTF8
    """

    with open(filename, "r", encoding="UTF8") as fichier:
        contenu = fichier.read()
        print(contenu.strip(),end="")
