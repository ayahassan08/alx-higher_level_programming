#!/usr/bin/python3
'''a function that writes a string to a text file (UTF8)'''


def write_file(filename="", text=""):
    '''Returns the number of characters written'''
    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))
