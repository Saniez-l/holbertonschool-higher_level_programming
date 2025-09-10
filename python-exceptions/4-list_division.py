#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    resultat = []

    for i in range(list_length):
        try:
            resultat.append(my_list_1[i] / my_list_2[i])

        except TypeError:
            print("wrong type")
            resultat.append(0)
        except ZeroDivisionError:
            print("division by 0")
            resultat.append(0)
        except IndexError:
            print("out of range")
            resultat.append(0)
        finally:
            continue
    return resultat
