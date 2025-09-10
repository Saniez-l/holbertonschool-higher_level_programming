#!/usr/bin/python3

def roman_to_int(roman_string):

    if type(roman_string) != str:
        return 0

    if len(roman_string) == 0:
        return 0
    a_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    valeur = []
    for key in roman_string:
        valeur.append(a_dic[key])

    return sum(valeur)
