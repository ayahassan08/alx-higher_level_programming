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
