#!/usr/bin/pytho3

def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    max_my_list = my_list[0]
    for number in my_list:
        if number > max_my_list:
            max_my_list = number
    return max_my_list
