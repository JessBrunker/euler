#!/usr/bin/python3

'''
What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
'''


def divisible(num):
    for i in range(20, 2, -1):
        if num % i != 0:
            return False
    return True

testnum = 2*3*5*7*11*13*17*19 

while not divisible(testnum):
    testnum += 6

print(testnum)
