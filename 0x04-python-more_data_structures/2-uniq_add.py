#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniSet = set()
    for element in my_list:
        uniSet.add(element)
    final = sum(uniSet)
    return final
