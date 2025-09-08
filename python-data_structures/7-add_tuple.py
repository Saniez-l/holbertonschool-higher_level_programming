#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = (tuple_a + (0, 0))[:2]
    tuple_b = (tuple_b + (0, 0))[:2]

    resultat_a = tuple_a[0] + tuple_b[0]
    resultat_b = tuple_a[1] + tuple_b[1]

    return resultat_a, resultat_b
