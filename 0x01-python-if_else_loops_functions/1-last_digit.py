#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
ldt = abs(number) % 10
if ldt > 5:
    print(f"Last digit of {number} is {ldt} and is greater than 5")
elif ldt == 0:
    print(f"Last digit of {number} is {ldt} and is zero")
elif ldt < 6 and ldt != 0:
    print(f"Last digit of {number} is {ldt} and is less than 6 and not zero")
