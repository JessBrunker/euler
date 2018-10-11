#!/usr/bin/python3

'''
What is the 10001st prime number?
'''

primes = [2]
prime_count = 1
testnum = 1

while prime_count != 10001:
    testnum += 2
    divisible = False
    for prime in primes:
        if testnum % prime == 0:
            divisible = True
            break
    if not divisible:
        primes.append(testnum)
        prime_count += 1

print(primes[-1])
