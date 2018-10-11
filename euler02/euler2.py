#!/usr/bin/python3

'''
Sum the even terms of the Fibonacci sequence up to four million
'''

a = 1
b = 2
c = 0
total = 2

while c <= 4000000:
    c = a + b
    a = b
    b = c

    if c % 2 == 0:
        total += c

print (total)
