#!/usr/bin/python3

'''
Let d(n) be defined as the sum of proper divisors of n (numbers less
than n which divide evenly into n).

If d(a) = b and d(b) = a, where a != b, then a and b are an amicable
pair and each of a and b are called amicable numbers.

For example the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55,110;
therefore d(220) = 284. The proper divisors of 284 are 1,2,4,71,142;
so d(284) = 220.

Evaluate the sum of all the amicable nubmers under 10000.
'''

import time


start = time.time()

# return a list of the divisors for a given number
def get_divisors(num):
    divisors = []
    limit = int(num/2) + 1
    for i in range(1, limit):
        if num % i == 0:
            divisors.append(i)
    return divisors


total = 0
nums = {} # number: sum(get_divisors(number))
for i in range(1, 10001):
    sum_divs = 0
    if i in nums: # d(n) has been found before
        sum_divs = nums[i]
    else: # need to find d(n)
        sum_divs = sum(get_divisors(i))
        nums[i] = sum_divs

    # lower numbers have all been checked, don't need to test
    if sum_divs <= i:
        continue

    sum_divs_2 = 0
    if sum_divs in nums:
        sum_divs_2 = nums[sum_divs]
    else:
        sum_divs_2 = sum(get_divisors(sum_divs))
        nums[sum_divs] = sum_divs_2
   
    # numbers are amicable
    if sum_divs_2 == i:
        total += i
        total += sum_divs



print(total)

end = time.time()
print('{}s'.format(end-start))
