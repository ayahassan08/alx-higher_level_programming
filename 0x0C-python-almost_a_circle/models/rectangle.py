#!/usr/bin/python3
'''Writes the class Rectangle that inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''A class constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width of rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Width setter'''
        self.__width = value

    @property
    def height(self):
        '''Height of rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Height setter'''
        self.__height = value

    @property
    def x(self):
        '''x of rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        self.__x = value

    @property
    def y(self):
        '''y of rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        self.__y = value
