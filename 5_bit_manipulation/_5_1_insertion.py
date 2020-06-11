def insertion(N, M, i, j):
  left_ones = -1 << (j+1)
  right_ones = (1 << i) - 1
  
  N &= (left_ones | right_ones)
  mask = M << i
  return N | mask

def test():
  N = 0b1000100100
  M = 0b0
  i, j = 5, 5
  print('PASS' if insertion(N, M, i, j) == 0b1000000100 else 'FAIL')
  
  N = 0b1000100100
  M = 0b1
  i, j = 5, 5
  print('PASS' if insertion(N, M, i, j) == 0b1000100100 else 'FAIL')
  
  N = 0b1000100100
  M = 0b0
  i, j = 4, 4
  print('PASS' if insertion(N, M, i, j) == 0b1000100100 else 'FAIL')
  
  N = 0b1000100100
  M = 0b1
  i, j = 4, 4
  print('PASS' if insertion(N, M, i, j) == 0b1000110100 else 'FAIL')
  
  N = 0b1000100100
  M = 0b11000
  i, j = 2, 6
  print('PASS' if insertion(N, M, i, j) == 0b1001100000 else 'FAIL')

if __name__ == "__main__":
  test()
