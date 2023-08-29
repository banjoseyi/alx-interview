#!/usr/bin/python3

""" function that returns the perimeter
of the island"""

def island_perimeter(grid):
  perimeter = 0
  i, j = len(grid), len(grid[0])
  
  for q in range(i):
    for r in range(j):
      if grid[q][r] == 1:
        perimeter += 4
        if q > 0 and grid[q-1][r] == 1:
          perimeter -= 2
        if r > 0 and grid[q][r-1] == 1:
          perimeter -= 2
  return perimeter
