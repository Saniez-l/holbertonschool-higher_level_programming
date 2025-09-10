#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        resultat = a / b
    except ZeroDivisionError:
        print("Inside result: None")
        return None
    else:
        print("Inside result: {:.1f}".format(resultat))
        return resultat
