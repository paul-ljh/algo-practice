'''
Write a method that find the maximum of 2 numbers. You should not use if-else or any other comparison operators.
'''

from math import log
from sys import maxsize

def number_max(n1, n2):
  d = n2 - n1  
  n1_sign = get_sign(n1)
  n2_sign = get_sign(n2)
  d_sign = get_sign(d)
  
  # 1 if same sign, 0 otherwise
  same_sign = int(n1_sign == n2_sign)

  # 1 if n2 is bigger or equal, 0 otherwise
  k = (1 - same_sign) * n2_sign + same_sign * d_sign

  return k * n2 + (1-k) * n1

# 1 if non-negative, 0 otherwise
def get_sign(n):
  sign_mask = 1 << 31
  return 1 - ((n & sign_mask) >> 31)

def test():
  
  n1, n2 = 3, 3
  print('PASS' if number_max(n1, n2) == 3 else 'FAIL')
  
  n1, n2 = 3, 4
  print('PASS' if number_max(n1, n2) == 4 else 'FAIL')
  
  n1, n2 = 2, 3
  print('PASS' if number_max(n1, n2) == 3 else 'FAIL')
  
  n1, n2 = -3, -3
  print('PASS' if number_max(n1, n2) == -3 else 'FAIL')
  
  n1, n2 = -3, -4
  print('PASS' if number_max(n1, n2) == -3 else 'FAIL')
  
  n1, n2 = -2, -3
  print('PASS' if number_max(n1, n2) == -2 else 'FAIL')
  
  n1, n2 = 2, -3
  print('PASS' if number_max(n1, n2) == 2 else 'FAIL')
  
  n1, n2 = -3, 4
  print('PASS' if number_max(n1, n2) == 4 else 'FAIL')
  
  n1, n2 = -3, maxsize
  print('PASS' if number_max(n1, n2) == maxsize else 'FAIL')
  
  n1, n2 = 3, -maxsize-1
  print('PASS' if number_max(n1, n2) == 3 else 'FAIL')

if __name__ == "__main__":
  test()
