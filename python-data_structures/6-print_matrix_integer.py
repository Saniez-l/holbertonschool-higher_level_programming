#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for liste in matrix:
        for i, element in enumerate(liste):
            if i < len(liste) - 1:
                print("{:d}" .format(element), end=" ")
            else:
                print("{:d}" .format(element), end="")
        print()
