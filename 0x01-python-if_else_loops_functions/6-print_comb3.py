#!/usr/bin/python3
for numbers in range(10):
    for number in range(numbers + 1, 10):
        print(f"{numbers}{number}", end=", " if numbers < 8 else "\n")
