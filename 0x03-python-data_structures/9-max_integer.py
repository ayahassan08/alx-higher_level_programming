#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    coList = my_list.copy()
    coList.sort()
    return coList[-1]
