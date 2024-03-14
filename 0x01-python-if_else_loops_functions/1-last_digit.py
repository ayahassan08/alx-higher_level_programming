#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
lasDigit = abs(number) % 10

if lasDigit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lasDigit))
elif lasDigit == 0:
    print("Last digit of {} is {} and is 0".format(number, lasDigit))
else:
    print(f"Last digit of {number} is {lasDigit} and is less than 6 and not 0")
