def sorted_matrix_search(matrix, target):
  if len(matrix) == 0:
    return None
  m, n = len(matrix), len(matrix[0])
  if target < matrix[0][0] or target > matrix[m-1][n-1]:
    return None
  
  r, c = m-1, 0
  while r >= 0 and c < n:
    if matrix[r][c] == target:
      return (r, c)
    elif matrix[r][c] > target:
      r -= 1
    else:
      c += 1
  return None

def test():
  m = []
  print('PASS' if sorted_matrix_search(m, 3) == None else 'FAIL')

  m = [[5, 6, 7]]
  print('PASS' if sorted_matrix_search(m, 3) == None else 'FAIL')

  m = [[5, 6, 7]]
  print('PASS' if sorted_matrix_search(m, 9) == None else 'FAIL')
  
  m = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
  ]
  print('PASS' if sorted_matrix_search(m, 15) == (0, 4) else 'FAIL')
  print('PASS' if sorted_matrix_search(m, 20) == None else 'FAIL')
  print('PASS' if sorted_matrix_search(m, 31) == None else 'FAIL')
  print('PASS' if sorted_matrix_search(m, 30) == (4, 4) else 'FAIL')
  print('PASS' if sorted_matrix_search(m, 0) == None else 'FAIL')
  print('PASS' if sorted_matrix_search(m, 1) == (0, 0) else 'FAIL')

if __name__ == '__main__':
  test()
