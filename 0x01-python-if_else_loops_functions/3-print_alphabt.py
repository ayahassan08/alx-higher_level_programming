#!/usr/bin/python3
for letters in range(ord('a'), ord('z') + 1):
    letter = chr(letters)
    if letter not in "qe":
        print(f"{letter}", end="")
