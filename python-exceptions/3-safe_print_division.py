#!/usr/bin/python3

def safe_print_division(a, b):
    resultat = None
    try:
        resultat = a / b
    except ZeroDivisionError:
        return None
    else:
        return resultat
    finally:
        if resultat is None:
            print("Inside result: None")
        else:
            print("Inside result: {:.1f}".format(resultat))
