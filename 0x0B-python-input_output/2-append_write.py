#!/usr/bin/python3
'''a function appends a string at the end of a text file (UTF8)'''


def append_write(filename="", text=""):
    '''Returns the number of characters added'''
    with open(filename, "a", encoding='utf-8') as file:
        return file.write(text)
