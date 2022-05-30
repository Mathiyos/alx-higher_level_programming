#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    num_1 = number % 10
else:
    num_1 = number % -10

print("Last digit of {} is {}".format(number, num_1), end='')

if num_1 > 5:
    print(" and is greater than 5")
elif num_1 == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
