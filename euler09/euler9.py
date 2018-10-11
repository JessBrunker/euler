#!/usr/bin/python3

'''
There exists only one Pythagorean triplet (a^2 + b^2 = c^2) for which
a + b + c = 1000.

Find the product abc.
'''

import math


for a in range(1, 1000):
    # don't need to check b < a because those are duplicates
    for b in range(a, 1000):
        c = math.sqrt(a**2 + b**2)
        if c != int(c): # is c an int?
            continue
        if a + b + c == 1000:
            print(a * b * c)
