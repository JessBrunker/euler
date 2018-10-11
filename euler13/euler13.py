#!/usr/bin/python3

'''
Work out the first ten digits of the 100 50-digit numbers.
'''

import time


start = time.time()

total = 0
with open('numbers') as f:
    for number in f:
        num = int(number)
        total += num

print (total)

end = time.time()
print('Time: {}s'.format(end-start))
