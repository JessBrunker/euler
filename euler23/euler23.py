#!/usr/bin/python3

'''
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1+2+4+7+14=28, which means 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is
less than n and it is called abundant if the sum exceed n.

As 12 is the smallest abundant number, 1+2+3+4+6=16, the smallest number
that can be written as the sum of two abundant numbers is 24. By
By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though
it is known that the greatest number that cannot be expressed as the sum
of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
'''

import time
import math


start = time.time()


summed_divisors = {1:0, 2:0, 3:0, 5:0, 7:0, 11:0, 13:0, 17:0, 19:0}

'''
def sum_divisors(num):
    if num in summed_divisors:
        return summed_divisors[num]
    top = int(num/2)
    while top > 1:
        if num % top == 0:
            div = int(num / top)
            factor = sum_divisors(top)
            summed_divisors[num] = 1 + top + factor
            if div not in summed_divisors:
                summed_divisors[num] += div
            return summed_divisors[num]
        top -= 1
    summed_divisors[num] = 0
    return 0
'''

def sum_divisors(num):
    if num == 1:
        return 1
    top = int(math.sqrt(num)) + 1
    total = 1
    divisor = 2
    while divisor < top:
        if num % divisor == 0:
            total += divisor
            total += int(num/divisor)
        divisor += 1
    return total

# test if number is abundant
def is_abundant(num):
    return sum_divisors(num)  > num


def test_abundant(num):
    total = 0
    for i in range(1, int(num/2)+1):
        if num % i == 0:
            total += i
    return total > num


if __name__ == '__main__':
    UPPER_LIMIT = 28124
    #UPPER_LIMIT = 2000
    abundants = []
    for i in range(2,UPPER_LIMIT, 2):
        if is_abundant(i):
            abundants.append(i)


    sums = set()
    top = 0
    for i in abundants:
        for j in abundants:
            total = i + j
            top = max(top, total)
            sums.add(total)

    total = 0
    for i in range(top):
        if i not in sums:
            total += i

    print(total)


end = time.time()
print('{}s'.format(end-start))
