#!/usr/bin/python3
'''a function returns the JSON representation of an object (string)'''
import json


def to_json_string(my_obj):
    '''Returns the JSON representation of an object'''
    return json.dumps(my_obj)
