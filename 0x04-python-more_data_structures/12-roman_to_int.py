#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    final = 0
    number = 0
    romanNum = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }
    for r in reversed(roman_string):
        number = romanNum[r]
        final += number if final < number * 5 else -number
    return final
