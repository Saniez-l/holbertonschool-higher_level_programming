#!/usr/bin/python3

def no_c(my_string):

    for charactere in "cC":
        my_string = my_string.replace(charactere, "")

    return my_string
