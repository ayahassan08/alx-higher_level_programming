#!/usr/bin/python3
"""To define a Locked Class"""

class LockedClass:
    """"To prevent the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name"""

    __slots__ = ("first_name")
