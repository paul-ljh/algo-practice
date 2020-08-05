'''
Imagine you have a square matrix, where each cell is either 1 or 0. Design an algorithm to find the maximum subsquare such that all four borders are filled with 1s.
'''

def max_black_square(square):
  length = len(square)
  row_sums = calculate_row_sums(square, length)
  col_sums = calculate_col_sums(square, length)
  max_top_right, max_size = None, 0
  for r in range(length):
    consecutive = 0
    for c in range(length):
      curr = square[r][c]
      if curr == 0:
        consecutive = 0
      else:
        consecutive += 1
        if (consecutive > max_size and check_3_borders(r, c, consecutive, row_sums, col_sums, length)):
          max_top_right, max_size = (r, c), consecutive
  return (max_top_right, max_size)

def check_3_borders(r, c, size, row_sums, col_sums, length):
  right = (((col_sums[r + size - 1][c] - (0 if r == 0 else col_sums[r - 1][c])) == size)
           if r + size - 1 < length
           else False)
  left = (((col_sums[r + size - 1][c - size + 1] -
            (0 if r == 0
            else col_sums[r - 1][c - size + 1]))
           == size)
          if r + size - 1 < length
          else False)
  bottom = (((row_sums[r + size - 1][c] - 
              (row_sums[r + size - 1][c - size] if c - size >= 0 else 0)) == size)
           if r + size - 1 < length
           else False)
  return right and left and bottom
  
def calculate_col_sums(square, length):
  col_sums = [[0] * length for _ in range(length)]
  for c in range(length):
    for r in range(length):
      col_sums[r][c] += square[r][c]
      col_sums[r][c] += (0 if r == 0 else col_sums[r-1][c])
  return col_sums

def calculate_row_sums(square, length):
  row_sums = [[0] * length for _ in range(length)]
  for r in range(length):
    for c in range(length):
      row_sums[r][c] += square[r][c]
      row_sums[r][c] += (0 if c == 0 else row_sums[r][c-1])
  return row_sums

def test():
  square = [[0]]
  answer = (None, 0)
  print('PASS' if max_black_square(square) == answer else 'FAIL')
  
  square = [[1]]
  answer = ((0,0), 1)
  print('PASS' if max_black_square(square) == answer else 'FAIL')
  
  square = [
    [0,0,0,0],
    [1,1,1,1],
    [1,0,1,1],
    [1,1,1,1],
  ]
  answer = ((1,2), 3)
  print('PASS' if max_black_square(square) == answer else 'FAIL')
  
  square = [
    [1,1,0,1,1],
    [0,0,0,0,0],
    [1,0,1,1,1],
    [1,0,1,1,0],
    [1,1,1,1,1],
  ]
  answer = ((2,3), 2)
  print('PASS' if max_black_square(square) == answer else 'FAIL')
  
  square = [
    [1,1,0,1,1],
    [0,0,0,0,0],
    [1,0,1,1,1],
    [1,0,0,1,0],
    [1,1,1,1,1],
  ]
  answer = ((0,0), 1)
  print('PASS' if max_black_square(square) == answer else 'FAIL')
  
  square = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,1,1,1],
    [1,0,0,1,1],
    [1,1,1,1,1],
  ]
  answer = ((0,4), 5)
  print('PASS' if max_black_square(square) == answer else 'FAIL')

if __name__ == "__main__":
  test()
