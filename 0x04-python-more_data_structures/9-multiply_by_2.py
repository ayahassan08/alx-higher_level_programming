#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    newDiction = {}
    for key, value in a_dictionary.items():
        newDiction[key] = value * 2
    return newDiction
