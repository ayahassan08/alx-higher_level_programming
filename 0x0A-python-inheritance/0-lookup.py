#!/usr/bin/python3
"""Defines Lookup Function."""

def lookup(obj):
	"""
	Returns a list of attributes and methods associated with the given object.
	"""
	return (dir(obj))
