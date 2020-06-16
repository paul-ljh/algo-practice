import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from math import log
from bit_ops import get_bit, set_bit

def next_number(num):
  return (get_prev(num), get_next(num))
  
def get_next(num):
  r = num
  l = int(log(num, 2)) + 1
  first_1 = first_0 = -1
  for i in range(l):
    curr = get_bit(num, i)
    if curr == 0 and first_1 != -1:
      r |= (1 << i)
      first_0 = i
      break
    if curr == 1 and first_1 == -1:
      first_1 = i
  
  if r == num:
    return -1

  zero_mask = -1 << first_0
  num_1s = first_0 - first_1 - 1
  one_mask = (1 << num_1s) - 1
  return r & zero_mask | one_mask

def get_prev(num):
  r = num
  l = int(log(num, 2)) + 1
  first_1 = first_0 = -1
  for i in range(l):
    curr = get_bit(num, i)
    if curr == 1 and first_0 >= 0:
      r ^= (1 << i)
      first_1 = i
      break
    if curr == 0 and first_0 == -1:
      first_0 = i
  
  if r == num:
    return -1

  zero_mask = (1 << first_0) - 1
  one_mask = ((1 << (first_0 + 1)) - 1) << (first_1 - first_0 - 1)
  return r ^ zero_mask | one_mask

def test():
  num = 0b1
  answer = (-1, -1)
  print('PASS' if next_number(num) == answer else 'FAIL')
  
  num = 0b1111
  answer = (-1, -1)
  print('PASS' if next_number(num) == answer else 'FAIL')
  
  num = 0b1000
  answer = (0b100, -1)
  print('PASS' if next_number(num) == answer else 'FAIL')
  
  num = 0b11100
  answer = (0b11010, -1)
  print('PASS' if next_number(num) == answer else 'FAIL')
  
  num = 0b1010101100
  answer = (0b1010101010, 0b1010110001)
  print('PASS' if next_number(num) == answer else 'FAIL')
  
  num = 0b10100111100
  answer = (0b10100111010, 0b10101000111)
  print('PASS' if next_number(num) == answer else 'FAIL')
  
  num = 0b1010100011
  answer = (0b1010011100, 0b1010100101)
  print('PASS' if next_number(num) == answer else 'FAIL')

if __name__ == "__main__":
  test()
