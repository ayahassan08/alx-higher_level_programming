#!/usr/bin/python3
'''a class Student that defines a student'''


class Student:
    '''Represents a student'''

    def __init__(self, first_name, last_name, age):
        '''Defines a student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Retrieves a dictionary representation of a Student instance'''
        return self.__dict__
