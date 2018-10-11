#!/usr/bin/python3

'''
In the 20x20 grid, what is the greatest product of four adjacent
numbers in the same direction (up, down, left, right, diagonal).
'''

grid = []

# open grid file and fill grid matrix
with open('grid') as f:
    for line in f:
        nums = line.split(' ')
        nums = [int(num) for num in nums]
        grid.append(nums)

biggest = 0
for row in range(20):
    for col in range(20):
        # check left to right
        if col + 3 < 20:
            num = grid[row][col] * \
                grid[row][col+1] * \
                grid[row][col+2] * \
                grid[row][col+3]
            biggest = max(biggest, num)
        # check up to down
        if row + 3 < 20:
            num = grid[row][col] * \
                grid[row+1][col] * \
                grid[row+2][col] * \
                grid[row+3][col]
            biggest = max(biggest, num)
        # check diagonal up-left to down-right
        if row + 3 < 20 and col + 3 < 20:
            num = grid[row][col] * \
                grid[row+1][col+1] * \
                grid[row+2][col+2] * \
                grid[row+3][col+3]
            biggest = max(biggest, num)
        # check diagonal up-right to down-left
        if row - 3 >= 0 and col + 3 < 20:
            num = grid[row][col] * \
                grid[row-1][col+1] * \
                grid[row-2][col+2] * \
                grid[row-3][col+3]
            biggest = max(biggest, num)

print(biggest)
