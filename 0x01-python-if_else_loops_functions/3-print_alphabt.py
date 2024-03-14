#!/usr/bin/python3
for letter in range(ord('a'), ord('z') + 1):
    excep = chr(letter)
    if excep not in "qe":
        print(excep, end="")
