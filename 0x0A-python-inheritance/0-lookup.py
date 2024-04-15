#!/usr/bin/python3
"""Defines Lookup Function."""

def lookup(obj):
	"""
	Returns a list of attributes and methods associated with the given object.

	Args:
		obj: a given object.

	Returns:
		list: a list of available attributes and methods of an object.
	"""
 
	return (dir(obj))
