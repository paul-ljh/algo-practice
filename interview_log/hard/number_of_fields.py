'''
TopHat, 2020 June 23

Number of Fields on the Farm

We want to count the number of fields on a farm, which is comprised of square patches which are either fertile or not, arranged in a grid. If there are fertile patches of land that are vertically or horizontally adjacent, they belong to the same field.

This can be represented by a 2-dimensional array of boolean values, with True signifying a fertile patch, and False signifying a patch of dirt. 

Create a function which accepts a 2-dimensional array and returns the number of fields present.

EX1:
  Input:
    T F T F
    F T T F
    F F F T

  Output:
    3
'''

import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from my_queue import Queue

def number_of_fields(land):
  rows, cols = len(land), len(land[0])
  count = 0
  for r in range(rows): 
    for c in range(cols):
      if land[r][c] == True:
        bfs(land, r, c, rows, cols)
        count += 1
  return count

def bfs(land, r, c, rows, cols):
  q = Queue()
  land[r][c] = False
  q.push((r, c))
  while not q.is_empty():
    x, y = q.pop()
    for i,j in [(x,y+1), (x,y-1), (x+1,y), (x-1,y)]:
      if i in range(rows) and j in range(cols) and land[i][j]:
        land[i][j] = False
        q.push((i,j))
  return

def test():
  land = [[False]]
  answer = 0
  print('PASS' if number_of_fields(land) == answer else 'FAIL')
  
  land = [[True]]
  answer = 1
  print('PASS' if number_of_fields(land) == answer else 'FAIL')
  
  land = [
    [True, False, True, False],
    [False, True, True, False],
    [False, False, False, True],
  ]
  answer = 3
  print('PASS' if number_of_fields(land) == answer else 'FAIL')
  
  land = [
    [True, True, True, False],
    [True, False, True, False],
    [True, True, True, True],
  ]
  answer = 1
  print('PASS' if number_of_fields(land) == answer else 'FAIL')
  
  land = [
    [False, True, True, True, True, True],
    [True, True, False, False, False, True],
    [True, False, True, False, False, True],
    [True, True, True, False, True, True],
  ]
  answer = 1
  print('PASS' if number_of_fields(land) == answer else 'FAIL')
  
  land = [
    [False, True, True, True, True, True, True],
    [True, True, False, False, False, False, True],
    [True, False, True, False, False, False, True],
    [True, False, True, False, True, False, True],
    [True, False, True, False, True, False, True],
    [True, True, True, False, True, True, True],
  ]
  answer = 1
  print('PASS' if number_of_fields(land) == answer else 'FAIL')
  
if __name__ == "__main__":
  test()
