#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maximum = 0
    for key, value in a_dictionary.items():
        if value > maximum:
            maximum = value
    for key, value in a_dictionary.items():
        if value == maximum:
            return key
