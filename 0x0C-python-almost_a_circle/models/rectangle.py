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
		self.validate_integer("width", value, False)
		self.__width = value

	@property
	def height(self):
		'''Height of rectangle'''
		return self.__height

	@height.setter
	def height(self, value):
		'''Height setter'''
		self.validate_integer("height", value, False)
		self.__height = value

	@property
	def x(self):
		'''x of rectangle'''
		return self.__x

	@x.setter
	def x(self, value):
		'''x setter'''
		self.validate_integer("x", value)
		self.__x = value

	@property
	def y(self):
		'''y of rectangle'''
		return self.__y

	@y.setter
	def y(self, value):
		'''y setter'''
		self.validate_integer("y", value)
		self.__y = value

	def validate_integer(self, name, value, eq=True):
		'''Adds validation of setter method and instantiation'''
		if type(value) != int:
			raise TypeError("{} must be an integer".format(name))
		if eq and value < 0:
			raise ValueError("{} must be >= 0".format(name))
		elif not eq and value <= 0:
			raise ValueError("{} must be > 0".format(name))

	def area(self):
		'''Returns the area value of the Rectangle'''
		return self.width * self.height
