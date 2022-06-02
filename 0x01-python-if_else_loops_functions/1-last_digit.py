#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
if number < 0:
    remainder = number % -10
else:
    remainder = number % 10
if remainder > 5:
    stri = "and is greater than 5"
elif remainder == 0:
    stri = "and is 0"
else:
    stri = "and is less than 6 and not 0"
print("Last digit of {0:d} is {1:d} {2:s}".format(number, remainder, stri))
