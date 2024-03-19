#!/usr/bin/python3

def no_c(my_string):
    new_str = ""
    for letters in my_string:
        if letters != "c" and letters != "C":
            new_str += letters
    return new_str
