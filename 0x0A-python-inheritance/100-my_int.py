#!/usr/bin/python3
"""
Defines a class MyInt that inherits from int.
"""


class MyInt(int):
    """version of an integer"""
    def __new__(cls, *args, **kwargs):
        """creates a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what used to be != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what used to be == is now !="""
        return int(self) == other
