'''
You have an integer matrix representing a plot of land, where the value at that location represents the height above sea level. A value of zero indicates water. A pond is a region of water connected vertically, horizontally, diagonally. The size of the pond is the total number of connected water cells. Write a method to compute the sizes of all ponds in the matrix.
'''

from queue import Queue

def dfs_pond_sizes(matrix):
  rows, cols = len(matrix), len(matrix[0])
  result = []
  for r in range(rows):
    for c in range(cols):
      if matrix[r][c] == 0:
        result.append(dfs(matrix, r, c))
  return result

def dfs(matrix, row, col):
  matrix[row][col] = None
  size = 1
  for r,c in [(row-1, col-1), (row-1, col), (row-1, col+1),
              (row, col-1), (row, col+1),
              (row+1, col-1), (row+1, col), (row+1, col+1)]:
    if r in range(len(matrix)) and c in range(len(matrix[0])) and matrix[r][c] == 0:
      size += dfs(matrix, r, c)
  return size

def bfs_pond_sizes(matrix):
  rows, cols = len(matrix), len(matrix[0])
  result = []
  for r in range(rows):
    for c in range(cols):
      if matrix[r][c] == 0:
        result.append(bfs(matrix, r, c))
  return result

def bfs(matrix, row, col):
  coord_queue = Queue()
  coord_queue.put((row, col))
  matrix[row][col] = None
  size = 1
  while not coord_queue.empty():
    init_r, init_c = coord_queue.get()
    for r,c in [(init_r-1, init_c-1), (init_r-1, init_c), (init_r-1, init_c+1),
              (init_r, init_c-1), (init_r, init_c+1),
              (init_r+1, init_c-1), (init_r+1, init_c), (init_r+1, init_c+1)]:
      if r in range(len(matrix)) and c in range(len(matrix[0])) and matrix[r][c] == 0:
        size += 1
        matrix[r][c] = None
        coord_queue.put((r,c))
  return size

def dfs_test():
  matrix = [[]]
  answer = []
  print('PASS' if dfs_pond_sizes(matrix) == answer else 'FAIL')
  
  matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
  ]
  answer = [9]
  print('PASS' if dfs_pond_sizes(matrix) == answer else 'FAIL')
  
  matrix = [
    [0,0,0],
    [1,0,1],
    [0,1,1],
  ]
  answer = [5]
  print('PASS' if dfs_pond_sizes(matrix) == answer else 'FAIL')
  
  matrix = [
    [0,2,1,0],
    [0,0,0,0],
    [1,1,1,1],
    [0,1,0,1]
  ]
  answer = [6,1,1]
  print('PASS' if dfs_pond_sizes(matrix) == answer else 'FAIL')
  

def bfs_test():
  matrix = [[]]
  answer = []
  print('PASS' if bfs_pond_sizes(matrix) == answer else 'FAIL')
  
  matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
  ]
  answer = [9]
  print('PASS' if bfs_pond_sizes(matrix) == answer else 'FAIL')
  
  matrix = [
    [0,0,0],
    [1,0,1],
    [0,1,1],
  ]
  answer = [5]
  print('PASS' if bfs_pond_sizes(matrix) == answer else 'FAIL')
  
  matrix = [
    [0,2,1,0],
    [0,0,0,0],
    [1,1,1,1],
    [0,1,0,1]
  ]
  answer = [6,1,1]
  print('PASS' if bfs_pond_sizes(matrix) == answer else 'FAIL')

if __name__ == "__main__":
  dfs_test()
  bfs_test()
