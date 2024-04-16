#!/usr/bin/python3
'''a class Student that defines a student'''


class Student:
    '''Represents a student'''

    def __init__(self, first_name, last_name, age):
        '''Defines a student'''
        self.firstName = first_name
        self.lastName = last_name
        self.age = age

    def to_json(self):
        '''Retrieves a dictionary representation of a Student instance'''
        return self
