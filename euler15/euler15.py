#!/usr/bin/python3

'''
Starting in the top left corner of a 2x2 grid, and only being able
to move to the right and down, there are exactly 6 routes to
the bottom right corner.

How many such routes are there through a 20x20 grid?
'''

import time


start = time.time()

EDGE = 20
grid = [[0 for i in range(EDGE+1)] for i in range(EDGE+1)]

# the number of paths to a specific cell resembles Pascal's triangle
for i in range(EDGE+1):
    grid[0][i] = 1
    grid[i][0] = 1

for row in range(1, EDGE+1):
    for col in range(1, EDGE+1):
        grid[row][col] = grid[row-1][col] + grid[row][col-1]


print(grid[-1][-1])

end = time.time()
print('{}s'.format(end-start))
