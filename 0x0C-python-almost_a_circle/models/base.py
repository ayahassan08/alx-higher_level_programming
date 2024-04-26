#!/usr/bin/python3
'''Defines a base model class.'''
from json import dumps, loads


class Base:
    '''Represents the base model.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''A class constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        '''Returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        '''Writes the JSON string representation of list_objs to a file'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))


