#!/usr/bin/python3

'''
The Collatz sequence is defined for the set of positive integers:
    n -> n/2 (n is even)
    n -> 3n+1 (n is odd)

Using the rules above and starting with 13, we get:
    13->40->20->10->5->16->8->4->2->1

The sequence contains 10 terms.

Which number under one million produces the longest chain?
'''

import time


start = time.time()

# hold the lengths for already found numbers
coll_dict = {1: 1}

# use the formula for a given number
def collatz(num):
    if num < 1:
        raise ValueError

    if num == 1:
        return 1
    c = 0
    if num % 2 == 0:
        c = num / 2
    else:
        c = (3 * num) + 1
    return int(c)

# recursively find the numbers of entries in the sequence
# also fill the coll_dict as it goes
def calc_sequence(num):
    if num in coll_dict:
        return coll_dict[num]
    else:
        collatz_num = collatz(num)
        coll_dict[num] = 1 + calc_sequence(collatz_num) 
        return coll_dict[num]


longest = 1
for i in range(3,1000000):
    test = calc_sequence(i)
    if coll_dict[i] > coll_dict[longest]:
        longest = i

print (longest)


end = time.time()
print('Time: {}s'.format(end-start))
