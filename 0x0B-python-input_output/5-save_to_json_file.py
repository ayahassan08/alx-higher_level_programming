#!/usr/bin/python3
'''a function writes an Object to a text file, using a JSON rep.'''
import json


def save_to_json_file(my_obj, filename):
    '''Writes an Object to a text file'''
    with open(filename, "w") as file:
        json.dump(my_obj, file)
