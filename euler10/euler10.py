#!/usr/bin/python3

'''
Find the sum of all primes below two million.
'''

import math


upper_limit = 2000000
primes = [2]
total = 2

for i in range(3, upper_limit, 2):
    is_prime = True
    for prime in primes:
        if prime > math.sqrt(i):
            break
        if i % prime == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
        total += i 

print(total)
