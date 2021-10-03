from sys import maxsize

def max_submatrix(matrix):
  n = len(matrix)
  if n == 0:
    return 0
  best = -maxsize-1
  dyna, sums = [0] * n, [0] * n
  for r1 in range(n):
    # recalculate the sums when base row moves
    for i in range(len(sums)):
      sums[i] = 0

    # based on the idea of 1D array dynamic programming
    for r2 in range(r1, n):
      for c in range(n):
        sums[c] += matrix[r2][c]
        dyna[c] = max(0, dyna[c-1] if c > 0 else 0) + sums[c]
        if dyna[c] > best:
          best = dyna[c]        
  return best

def test():  
  matrix = [
    [1],
  ]
  print('PASS' if max_submatrix(matrix) == 1 else 'FAIL')
  
  matrix = [
    [-1,-2],
    [-3,-4]
  ]
  print('PASS' if max_submatrix(matrix) == -1 else 'FAIL')

  matrix = [
    [4,1,2,-4],
    [-4,5,-10,6],
    [12,1,4,-5],
    [6,7,-10,2]
  ]
  print('PASS' if max_submatrix(matrix) == 32 else 'FAIL')
  
  matrix = [
    [4,0,2,-4],
    [5,2,3,-10],
    [-1,-5,4,8],
    [15,12,1,2]
  ]
  print('PASS' if max_submatrix(matrix) == 42 else 'FAIL')
  
if __name__ == '__main__':
  test()
