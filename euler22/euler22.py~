#!/usr/bin/python3

'''
Using names.txt, a file containing over 5000 first names, begin by
sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position
in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3+15+12+9+14=53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
'''

import time
import re


start = time.time()


# read through file, clean up names, return names as sorted list
def slurp_names():
    names = ''
    with open('names.txt') as f:
        names = f.readlines()[0]
        names = re.sub('"', '', names)
        names = names.split(',')
    return sorted(names)


# return the value of a letter using its ascii value
def get_char_value(char):
    return ord(char) - 64 # 'A' = 65, 'Z' = 90


# return the sum of character values in a name
def get_name_value(name):
    total = 0
    for char in name:
        total += get_char_value(char)
    return total


names = slurp_names()
total = 0
for i in range(len(names)):
    name_value = get_name_value(names[i])
    total += name_value * (i+1) 

print(total)


end = time.time()
print('{}s'.format(end-start))
