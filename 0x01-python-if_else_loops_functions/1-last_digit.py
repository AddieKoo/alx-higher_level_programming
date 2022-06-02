#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
str1 = "Last digit of"
str2 = "is"
str3 = "and is greater than 5"
str4 = "and is 0"
str5 = "and is less than 6 and not 0"
if number > 0:
    ldt = number % 10
elif number < 0:
    ldt = number % -10
print('Last digit of', number, 'is', ldt, end=' ')
if ldt > 5:
    print('and is greater than 5')
elif ldt == 0:
    print('and is 0')
elif ldt < 6 and ldt != 0:
    print('and is less than 6 and not 0')
