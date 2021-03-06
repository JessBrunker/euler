#!/usr/bin/python3

'''
By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.
                 3
                7 4
               2 4 6
              8 5 9 3
That is, 3+7+4+9=23.

Find the maximum total from top to bottom of the triangle (in file)
'''

import time

start = time.time()


triangle = []
with open('triangle') as f:
    for line in f:
        nums = line.split(' ')
        triangle.append([int(num) for num in line.split(' ')])

# count up from bottom of triangle, skipping bottom row
for row in range(len(triangle)-2, -1, -1):
    for i in range(len(triangle[row])):
        # find if adding to the lower left or right is bigger
        l_test = triangle[row][i] + triangle[row+1][i]
        r_test = triangle[row][i] + triangle[row+1][i+1]
        # collapse the bigger value upward into this cell
        triangle[row][i] = max(l_test, r_test)

# the top value is the best path through the triangle
print(triangle[0][0])

end = time.time()
print('{}s'.format(end-start))
