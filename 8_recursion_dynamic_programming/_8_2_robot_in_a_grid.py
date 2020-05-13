def robot_in_a_grid(grid):
  if not grid:
    return None
  visited = create_visit_grid(grid)
  return find_path(grid, visited, len(grid)-1, len(grid[0])-1)

# 2-D array for guaranteed O(1) look-up time, or u can use hash of tuples
def create_visit_grid(grid):
  visited = [[False] * len(grid[0]) for i in range(len(grid))]
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      visited[row][col] = grid[row][col] == 1
  return visited

def find_path(grid, visited, row, col):
  if visited[row][col]:
    return None
  visited[row][col] = True
  if row == col == 0:
    return [(row, col)]
  if row - 1 >= 0:
    p = find_path(grid, visited, row-1, col)
    if p:
      return p + [(row, col)]
  if col - 1 >= 0:
    p = find_path(grid, visited, row, col-1)
    if p:
      return p + [(row, col)]
  return None

def test():
  grid = []
  print('PASS' if robot_in_a_grid(grid) is None else 'FAIL')
  
  grid = [[1]]
  print('PASS' if robot_in_a_grid(grid) is None else 'FAIL')
  
  grid = [[0]]
  print('PASS' if robot_in_a_grid(grid) == [(0,0)] else 'FAIL')
  
  grid = [[0], [0]]
  print('PASS' if robot_in_a_grid(grid) == [(0,0), (1,0)] else 'FAIL')
  
  grid = [[0,1,0,0,0],
          [0,0,0,1,0],
          [0,1,0,0,1],
          [0,0,1,0,0]]
  print('PASS' if robot_in_a_grid(grid) == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4)] else 'FAIL')
  
  grid = [[0,1,0,0,0],
          [0,1,0,1,0],
          [0,1,0,0,1],
          [0,0,1,0,0]]
  print('PASS' if robot_in_a_grid(grid) is None else 'FAIL')
  
  grid = [[1,1,0,0,0],
          [0,0,0,1,0],
          [0,1,0,0,1],
          [0,0,1,0,0]]
  print('PASS' if robot_in_a_grid(grid) is None else 'FAIL')
  
  grid = [[0,1,0,0,0],
          [0,0,0,1,0],
          [0,1,0,0,1],
          [0,0,1,0,1]]
  print('PASS' if robot_in_a_grid(grid) is None else 'FAIL')

if __name__ == '__main__':
  test()
