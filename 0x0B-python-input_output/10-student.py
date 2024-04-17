#!/usr/bin/python3
'''a class Student defines a student by: (based on 9-student.py)'''


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        '''Defines a new Student.'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Get a dict. representation of the Student.'''
        if (type(attrs) == list and all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
