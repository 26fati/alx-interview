#!/usr/bin/python3
"""Module to define a function island_perimeter"""


def island_perimeter(grid):
    ''' a function that returns the perimeter
        of the island described in grid
    '''
    total = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                total += 4
                if x > 0:
                    total = total - grid[x-1][y] * 2
                if y > 0:
                    total = total - grid[x][y-1] * 2
    return total
