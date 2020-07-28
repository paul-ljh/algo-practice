'''
DataBricks, 2020 June 24

Your students are getting craftier and hiding words in 2D grids of letters. The word may start anywhere in the grid, and consecutive letters can be either immediately below or immediately to the right of the previous letter.

Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates. If there are multiple matches, return any one.

grid1 = [
    ['c', 'c', 'c', 'a', 'r', 's'],
    ['c', 'c', 'i', 't', 'n', 'b'],
    ['a', 'c', 'n', 'n', 't', 'i'],
    ['t', 'c', 'i', 'i', 'p', 't']
]

word1_1 = "catnip"
find_word_location(grid1, word1_1)-> [ (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 4) ]

word1_2 = "cccc"
find_word_location(grid1, word1_1)-> [(0, 1), (1, 1), (2, 1), (3, 1)]
OR [(0, 0), (1, 0), (1, 1), (2, 1)]
OR [(0, 0), (0, 1), (1, 1), (2, 1)]
OR [(1, 0), (1, 1), (2, 1), (3, 1)]


grid2 = [
    ['c', 'p', 'a', 'n', 't', 's'],
    ['a', 'b', 'i', 't', 'a', 'b'],
    ['t', 'f', 'n', 'n', 'c', 'i'],
    ['x', 's', 'c', 'a', 't', 'n'],
    ['x', 's', 'd', 'd', 'e', 'a'],
    ['s', 'q', 'w', 'x', 's', 'p']
]

word2 = "catnap"
find_word_location(grid2, word2)-> [ (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5) ]


grid3 = [
    ['c', 'r', 'c', 'a', 'r', 's'],
    ['a', 'b', 'i', 't', 'n', 'i'],
    ['t', 'f', 'n', 'n', 'x', 'p'],
    ['x', 's', 'i', 'x', 'p', 't']]
word3 = "catnip"
find_word_location(grid3, word3)-> [ (0, 2), (0, 3), (1, 3), (1, 4), (1, 5), (2, 5) ]

n = number of rows
m = number of columns
w = length of the word
'''

import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from bit_ops import get_bit, set_bit

def find_word_in_grid(grid, word):
  rows, cols = len(grid), len(grid[0])
  visited = [[0] * cols for _ in range(rows)]
  for r in range(rows):
    for c in range(cols):
      result = dfs(grid, visited, word, 0, r, c)
      if result:
        return list(reversed(result))
  return None

def dfs(grid, visited, word, index, r, c):
  visited[r][c] = set_bit(visited[r][c], index)
  if grid[r][c] != word[index]:
    return False
  elif index == len(word)-1:
    return [(r,c)]
  
  for x,y in [(r+1, c), (r, c+1)]:
    if x < len(grid) and y < len(grid[0]) and not get_bit(visited[x][y], index+1):
      result = dfs(grid, visited, word, index+1, x, y)
      if result != False:
        result.append((r,c))
        return result
  return False

def test():
  grid = [
      ['c', 'c', 'b'],
      ['c', 'a', 't'],
      ['d', 't', 't'],
      ['d', 't', 'e']
  ]
  word = 'c'
  answer = [(0,0)]
  print('PASS' if find_word_in_grid(grid, word) == answer else 'FAIL')
  
  word = 'a'
  answer = [(1,1)]
  print('PASS' if find_word_in_grid(grid, word) == answer else 'FAIL')
  
  word = 'x'
  answer = None
  print('PASS' if find_word_in_grid(grid, word) == answer else 'FAIL')
  
  word = 'ca'
  answer = [(0,1), (1,1)]
  print('PASS' if find_word_in_grid(grid, word) == answer else 'FAIL')
  
  word = 'te'
  answer = [(2,2), (3,2)]
  print('PASS' if find_word_in_grid(grid, word) == answer else 'FAIL')
  
  word = 'eat'
  answer = None
  print('PASS' if find_word_in_grid(grid, word) == answer else 'FAIL')
  
  word = 'tta'
  answer = None
  print('PASS' if find_word_in_grid(grid, word) == answer else 'FAIL')
  
  word = 'ccatte'
  answer = [(0,0), (1,0), (1,1), (2,1), (3,1), (3,2)]
  print('PASS' if find_word_in_grid(grid, word) == answer else 'FAIL')

if __name__ == "__main__":
  test()
