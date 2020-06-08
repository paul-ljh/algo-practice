def n_queens(n):
  if n == 0:
    return []
  final_result = []
  arrange_queens(0, 0, 0, 0, n, [0]*n, final_result)
  return final_result

def arrange_queens(row, col_opts, diff_opts, sum_opts, n, curr_result, final_result):
  if row == n:
    final_result.append(curr_result.copy())
  else:
    for col in range(n):
      d,s = row-col, row+col
      if is_valid_coordinate(row, col, col_opts, diff_opts, sum_opts, n):
        curr_result[row] = col
        arrange_queens(row+1,
                       col_opts | (1 << col),
                       diff_opts | (1 << d+n),
                       sum_opts | (1 << s),
                       n,
                       curr_result, final_result)
          
def is_valid_coordinate(row, col, col_opts, diff_opts, sum_opts, n):
  d,s = row-col, row+col
  return (col_opts & (1 << col) == 0 and
          diff_opts & (1 << d+n) == 0 and
          sum_opts & (1 << s) == 0)
  

def test():
  n = 1
  print('PASS' if n_queens(n) == [[0]] else 'FAIL')
  
  n = 2
  print('PASS' if n_queens(n) == [] else 'FAIL')
  
  n = 3
  print('PASS' if n_queens(n) == [] else 'FAIL')
  
  n = 4
  print('PASS' if n_queens(n) == [
      [1,3,0,2],
      [2,0,3,1],
    ] else 'FAIL')
  
  n = 5
  print('PASS' if n_queens(n) == [[0, 2, 4, 1, 3],
    [0, 3, 1, 4, 2],
    [1, 3, 0, 2, 4],
    [1, 4, 2, 0, 3],
    [2, 0, 3, 1, 4],
    [2, 4, 1, 3, 0],
    [3, 0, 2, 4, 1],
    [3, 1, 4, 2, 0],
    [4, 1, 3, 0, 2],
    [4, 2, 0, 3, 1],
  ] else 'FAIL')
  
  n = 6
  print('PASS' if n_queens(n) == [
    [1, 3, 5, 0, 2, 4], 
    [2, 5, 1, 4, 0, 3], 
    [3, 0, 4, 1, 5, 2], 
    [4, 2, 0, 5, 3, 1],
  ] else 'FAIL')
  
if __name__ == '__main__':
  test()
