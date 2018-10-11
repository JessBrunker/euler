#!/usr/bin/python3

'''
n! means n * (n-1) * ... * 3 * 2 * 1

For example, 10! = 3628800,
and the sum of the digits in the number 10! is 3+6+2+8+8+0+0=27.

Find the sum of the digits in the number 100!
'''


import time


start = time.time()

# calculate the factorial of a given number
def factorial(num):
    total = 1
    while num > 1:
        total *= num
        num -= 1
    return total

# convert factorial to a string, then loop through adding digits
num = str(factorial(100))
total = 0
for digit in num:
    total += int(digit)

print (total)


end = time.time()
print('{}s'.format(end-start))
