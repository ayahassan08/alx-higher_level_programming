#!/usr/bin/python3

"""Defines an object attribute lookup function."""


def lookup(obj):
	"""Returns a list of attributes and methods of a given object."""
	return (dir(obj))
