'''
Google Japan, Software Engineer New Grad, 2020 June

Given a 2D matrix, determine whether one can walk from, the top left cornor of coordinate (0,0), to the bottom right cornor of coordinate (rows-1, cols-1), with the contraint that you can only walk to an element less than or equal to the current element.

EX:
[
  [1,2],
  [3,4],
]
 => False

[
  [4,2],
  [3,1],
]
 => True
'''

def matrix_traversal(matrix, visited, r, c):
  rows, cols = len(matrix), len(matrix[0])
  if (r,c) == (rows-1, cols-1):
    return True
  
  visited[r][c] = -1
  for x,y in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
    if (x in range(rows) and
        y in range(cols) and
        visited[x][y] == 0 and
        matrix[x][y] <= matrix[r][c]):
      if matrix_traversal(matrix, visited, x, y):
        return True

  visited[r][c] = 1
  return False

def walk_matrix(matrix):
  rows, cols = len(matrix), len(matrix[0])
  visited = [[0] * cols for _ in range(rows)]
  return matrix_traversal(matrix, visited, 0, 0)

def test():
  matrix = [
    [1,2],
    [3,4],
  ]
  answer = False
  print('PASS' if walk_matrix(matrix) == answer else 'FAIL')
  
  matrix = [
    [4,2],
    [3,1],
  ]
  answer = True
  print('PASS' if walk_matrix(matrix) == answer else 'FAIL')
  
  matrix = [
    [8,9,9,7,7,7,7],
    [8,9,9,7,9,9,7],
    [8,9,9,7,7,9,7],
    [8,8,9,9,7,9,7],
    [9,8,8,8,7,9,7],
    [9,9,9,9,9,9,7],
  ]
  answer = True
  print('PASS' if walk_matrix(matrix) == answer else 'FAIL')

  matrix = [
    [7,7,7,9],
    [7,9,7,9],
    [7,9,7,9],
    [7,7,7,9],
    [7,7,9,9],
    [9,7,7,7],
  ]
  answer = True
  print('PASS' if walk_matrix(matrix) == answer else 'FAIL')
  
  matrix = [
    [7,7,7,9],
    [7,9,7,9],
    [7,9,7,9],
    [7,7,7,9],
    [7,9,9,9],
    [9,7,7,7],
  ]
  answer = False
  print('PASS' if walk_matrix(matrix) == answer else 'FAIL')

if __name__ == "__main__":
  test()
