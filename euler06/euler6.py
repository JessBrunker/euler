#!/usr/bin/python3

'''
Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
'''


sum_of_squares = 0
sums = 0
for i in range(1, 101):
    sum_of_squares += i**2
    sums += i 

sums = sums**2

print(sums - sum_of_squares)
