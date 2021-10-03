'''
Design an algorithm to figure out if someone has won a game of tic-tac-toe, where player 1 is 1, player 2 is 2, unplayed 0.
'''

class Coordinate:
  def __init__(self, row, col, row_incre, col_incre, length):
    self.row = row
    self.col = col
    self.row_incre = row_incre
    self.col_incre = col_incre
    self.length = length
    
  def get_curr(self):
    return (self.row, self.col)
  
  def increment(self):
    self.row += self.row_incre
    self.col += self.col_incre
    return
  
  def in_bound(self):
    length_range = range(self.length)
    return self.row in length_range and self.col in length_range

def tic_tac_win(grid):
  length = len(grid)
  search_list = []
  for i in range(length):
    search_list.append(Coordinate(0, i, 1, 0, length)) # Vertiical Line
    search_list.append(Coordinate(i, 0, 0, 1, length)) # Horizontal Line
  search_list.append(Coordinate(0, 0, 1, 1, length)) # Top-left to Bottom-right
  search_list.append(Coordinate(0, length-1, 1, -1, length)) # Top-right to Bottom-left
  
  for coord in search_list:
    if search_line(grid, coord):
      return True
  return False
  
def search_line(grid, coord):
  row, col = coord.get_curr()
  first = grid[row][col]
  if first == 0:
    return False
  while coord.in_bound():
    row, col = coord.get_curr()
    if grid[row][col] != first:
      return False
    coord.increment()
  return True

def test():
  grid = [[0]]
  answer = False
  print('PASS' if tic_tac_win(grid) == answer else 'FAIL')

  grid = [[1]]
  answer = True
  print('PASS' if tic_tac_win(grid) == answer else 'FAIL')
  
  grid = [
    [1,1,1,1],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
  ]
  answer = True
  print('PASS' if tic_tac_win(grid) == answer else 'FAIL')
  
  grid = [
    [1,1,1,2],
    [0,0,0,2],
    [0,0,0,2],
    [0,0,0,2],
  ]
  answer = True
  print('PASS' if tic_tac_win(grid) == answer else 'FAIL')
  
  grid = [
    [1,1,1,2],
    [0,0,2,1],
    [0,2,0,1],
    [2,0,0,1],
  ]
  answer = True
  print('PASS' if tic_tac_win(grid) == answer else 'FAIL')
  
  grid = [
    [1,1,1,0],
    [0,1,2,1],
    [0,2,1,1],
    [2,0,0,1],
  ]
  answer = True
  print('PASS' if tic_tac_win(grid) == answer else 'FAIL')
  
  grid = [
    [1,1,1,0],
    [0,0,2,1],
    [0,2,0,1],
    [2,0,0,1],
  ]
  answer = False
  print('PASS' if tic_tac_win(grid) == answer else 'FAIL')
  

if __name__ == "__main__":
  test()


  