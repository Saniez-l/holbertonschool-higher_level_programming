#!/usr/bin/python3
"""
Module for read file
"""

def read_file(filename=""):
    """
    Read file with open
    """

    with open(filename, "r") as fichier:
        contenu = fichier.read()
        print(contenu.strip(),end="")
