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

    def width(self):
        '''Width of rectangle'''
        return self.__width

    def width(self, value):
        '''Width setter'''
        self.validate_integer("width", value, False)
        self.__width = value

    def height(self):
        '''Height of rectangle'''
        return self.__height

    def height(self, value):
        '''Height setter'''
        self.validate_integer("height", value, False)
        self.__height = value

    def x(self):
        '''x of rectangle'''
        return self.__x

    def x(self, value):
        '''x setter'''
        self.validate_integer("x", value)
        self.__x = value

    def y(self):
        '''y of rectangle'''
        return self.__y

    def y(self, value):
        '''y setter'''
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''Adds validation of setter method and instantiation'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''Returns the area value of the Rectangle'''
        return self.width * self.height

    def display(self):
        '''Prints in stdout the Rectangle with the character #'''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        '''Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''A method'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Assigns an argument to each attribute'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns the dictionary representation of a Rectangle'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
