#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    elm_a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    elm_a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    elm_b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    elm_b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (elm_a1 + elm_b1, elm_a2 + elm_b2)
