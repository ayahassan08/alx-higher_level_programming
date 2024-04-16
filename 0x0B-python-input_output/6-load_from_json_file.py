#!/usr/bin/python3
'''a function that creates an Object from a JSON file'''
import json


def load_from_json_file(filename):
    '''Creates an object'''
    with open(filename) as file:
        return json.load(file)
