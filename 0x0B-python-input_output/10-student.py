#!/usr/bin/python3
'''a class Student defines a student by: (based on 9-student.py)'''


class Student:
	'''Represents a student'''

	def __init__(self, first_name, last_name, age):
		'''Defines a student'''
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def to_json(self, attrs=None):
     '''Retrieves a dictionary representation of a Student instance'''
		try:
			for attr in attrs:
				if type (attr) is not str:
					return self._dict_
		except Exception:
			return self._dict_
		my_dict = dict()
		for key, value in self._dict__.items():
			if key in attrs:
				my_dict[key] = value
		return my_dict
