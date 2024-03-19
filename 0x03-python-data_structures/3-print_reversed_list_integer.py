#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    new_list = my_list.sort(reverse=True)
    for number in my_list:
        print("{:d}".format(number))
