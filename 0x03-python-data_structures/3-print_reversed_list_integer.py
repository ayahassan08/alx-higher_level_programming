#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    new_list = my_list.sort(reverse=True)
    for number in my_list:
        print("{:d}".format(number))
