#!/usr/bin/python3

'''
Sum up all the multiples of 3 or 5 below 1000.
'''

total = 0

for i in range(3,1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(total)
