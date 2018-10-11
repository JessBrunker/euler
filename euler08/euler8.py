#!/usr/bin/python3

'''
Find the thirteen adjacent digits in the 1000-digit number that
have the greatest product.
'''

# the 1000-digit number is stored in the file 'num'
num = open('num', 'r').read()

index = 0
biggest = 0
for i in range(len(num)):
    test_num = num[i:i+13]
    if len(test_num) < 13:
        break
    total = 1
    for digit in test_num:
        total *= int(digit)
    if total > biggest:
        index = i
        biggest = total

print(biggest)
