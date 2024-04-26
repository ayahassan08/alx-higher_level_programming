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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Jsonifies a dictionary so it's quite rightly and longer.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
