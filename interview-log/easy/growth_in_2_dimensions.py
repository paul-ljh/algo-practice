'''
IXL Learning, 2020.5

Start with an infinite 2D grid filled with zeros, indexed from (1,1) at the bottom left cornor with coordinates increasing toward the top and right.

Given a series of coordinates (r,c) where r is the ending row and c is the ending column, add 1 to each element in the range from (1,1) to (r,c) inclusive. Once all coordinates are processed, determine how many cells contain the maximum value in the grid.

EX:
0,0,0             0,0,0             0,0,0
0,0,0 -> (1,2) -> 0,0,0 -> (2,2) -> 1,1,0
0,0,0             1,1,0             2,2,0

'''

from sys import maxsize

def growth_in_2d(coordinates):
  overlap = (maxsize, maxsize)
  for x,y in coordinates:
    overlap = (min(x, overlap[0]), min(y, overlap[1]))
  return overlap[0] * overlap[1]
  
def test():
  coordinates = [(1,1), (1,1), (1,1), (1,1), (1,1)]
  print('PASS' if growth_in_2d(coordinates) == 1 else 'FAIL')
  
  coordinates = [(2,1), (2,2), (3,3), (2,2), (3,3)]
  print('PASS' if growth_in_2d(coordinates) == 2 else 'FAIL')
  
  coordinates = [(3,3), (2,2), (3,3), (2,2), (3,3)]
  print('PASS' if growth_in_2d(coordinates) == 4 else 'FAIL')

if __name__ == '__main__':
  test()
