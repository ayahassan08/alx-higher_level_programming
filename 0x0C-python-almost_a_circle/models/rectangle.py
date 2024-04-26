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
