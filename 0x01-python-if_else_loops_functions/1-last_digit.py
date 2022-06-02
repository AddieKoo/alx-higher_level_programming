#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
str1 = "Last digit of"
str2 = "is"
str3 = "and is greater than 5"
str4 = "and is 0"
str5 = "and is less than 6 and not 0"
ldt = abs(number) % 10
if ldt > 5:
    print(f"{str1} {number} {str2} {ldt} {str3}")
elif ldt == 0:
    print(f"{str1} {number} {str2} {ldt} {str4}")
elif ldt < 6 and ldt != 0:
    print(f"{str1} {number} {str2} {ldt} {str5}")
