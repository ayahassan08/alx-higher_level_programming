#!/usr/bin/python3
"""Lookup method."""
def lookup(obj):
	"""
	Args:
		a given object.
 
	Returns:
		a list of available attributes and methods of an object.
	"""
	return (dir(obj))
