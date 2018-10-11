#!/usr/bin/python3

'''
What is the largest prime factor of 600851475143?
'''

import math


goal_num = 600851475143

def is_prime(num):
    if num % 2 == 0:
        return True

    for i in range(3, int(math.sqrt(num)), 2):
        if num % i == 0:
            return False

    return True

upper_bound = int(math.sqrt(goal_num))
if upper_bound % 2 == 0:
    upper_bound -= 1

for i in range(upper_bound, 2, -2):
    if goal_num % i == 0:
        if is_prime(i):
            print(i)
            break
