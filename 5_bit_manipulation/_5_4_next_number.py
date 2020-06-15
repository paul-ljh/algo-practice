import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from math import log
from bit_ops import get_bit, set_bit

def next_number(num):
  lg, sm = num, num
  l = int(log(num, 2)) + 1
  first_1 = -1
  for i in range(l):
    curr = get_bit(num, i)
    if curr == 0 and first_1 >= 0:
      lg ^= (1 << first_1)
      lg |= (1 << i)
      first_1 += 1
      if sm == num:
        sm = num ^ (1 << (i-1)) | (1 << i)

    if curr == 1 and first_1 == -1:
      first_1 = i
  return (sm, lg)

def test():
  num = 0b1
  answer = (0b1, 0b1)
  print('PASS' if next_number(num) == answer else 'FAIL')
  
  num = 0b1000
  answer = (0b1000, 0b1000)
  print('PASS' if next_number(num) == answer else 'FAIL')
  
  num = 0b11100
  answer = (0b11100, 0b11100)
  print('PASS' if next_number(num) == answer else 'FAIL')
  
  num = 0b1010101100
  answer = (0b1010110100, 0b1111100000)
  print('PASS' if next_number(num) == answer else 'FAIL')

if __name__ == "__main__":
  test()
