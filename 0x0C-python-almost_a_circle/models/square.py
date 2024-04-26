#!/usr/bin/python3
'''Write the class Square that inherits from Rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''A class constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string info'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Size of square'''
        return self.width

    @size.setter
    def size(self, value):
        '''Size setter'''
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''A method'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Assigns attributes'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
