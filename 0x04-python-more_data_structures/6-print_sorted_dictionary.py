#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sortKeys = sorted(a_dictionary.keys())
    for key in sortKeys:
        print("{}: {}".format(key, a_dictionary[key]))
