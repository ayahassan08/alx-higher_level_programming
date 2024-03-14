#!/usr/bin/env python3
def uppercase(str):
    for letter in str:
        if 'a' <= letter <= 'z':
            upLetter = chr(ord(letter) - ord('a') + ord('A'))
            print(upLetter, end="")
        else:
            print(letter, end="")
    
    print()
