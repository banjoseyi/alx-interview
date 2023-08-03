#!/usr/bin/python3

"""Program that solves the N queens problem"""
import sys


if __name__ == '__main__':
  code = sys.argv
  if len(code) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
    
  try:
    n = int(code[1])
  except ValueError:
    print('N must be a number')
    exit(1)
    
  if n < 4:
    print('N must be at least 4')
    exit(1)
    
  column = 0
  row = 0
  stop = False
  result = []
  queenPosition = []
    
  while row < n:
    reverse = False
    while column < n:
        
      safe = True
      for post in queenPosition:
        p = post[1]
        if (p == column or p + (row-post[0]) == column or p - (row-post[0]) == column):
          safe = False
          break
        
        if not safe:
          if column == n - 1:
            reverse = True
            break
          column = column + 1
          continue
        
        
        posts = [row, column]
        queenPosition.append(posts)
        
        if row == n -1:
          result.append(queenPosition[:])
          for post in queenPosition:
            if post[1] < n - 1:
              row = post[0]
              column = post[1]
          for r in range(n - row):
            queenPosition.pop()
          if row == n - 1 and column == n - 1:
            queenPosition = []
            stop = True
            
          row = row - 1
          column = column + 1
          
        else:
          column = 0
        break
      
      if stop:
        break
      
      if reverse:
        row = row - 1
        while row >= 0:
          column = queenPosition[row][1] + 1
          del queenPosition[row]
          if column < n:
            break
          row = row - 1
        if row < 0:
          break
        continue
      row = row + 1
      
    for idx, val in enumerate(result):
      if idx == len(result) - 1:
        print(val)
      else:
        print(val)
