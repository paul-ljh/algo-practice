import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from math import log
from bit_ops import get_bit, set_bit

def flip_bit_to_win(num):
  if num == 0:
    return 1
  l = int(log(num, 2)) + 1
  if num + 1 == 1 << l:
    return l

  max_l, prev_l, curr_l = 1,0,0
  for i in range(l):
    curr = get_bit(num, i)
    nex = get_bit(num, i+1)
    if curr == 0:
      prev_l = curr_l if nex == 1 else 0
      curr_l = 0
    else:
      curr_l += 1
    max_l = max(max_l, curr_l+prev_l+1)
  return max_l

def test():
  num = 0b0
  print('PASS' if flip_bit_to_win(num) == 1 else 'FAIL')
  
  num = 0b1
  print('PASS' if flip_bit_to_win(num) == 1 else 'FAIL')
  
  num = 0b11111
  print('PASS' if flip_bit_to_win(num) == 5 else 'FAIL')
  
  num = 0b1110
  print('PASS' if flip_bit_to_win(num) == 4 else 'FAIL')
  
  num = 0b10111
  print('PASS' if flip_bit_to_win(num) == 5 else 'FAIL')
  
  num = 0b100111
  print('PASS' if flip_bit_to_win(num) == 4 else 'FAIL')
  
  num = 0b100110111
  print('PASS' if flip_bit_to_win(num) == 6 else 'FAIL')
  
  num = 0b110110111111100011
  print('PASS' if flip_bit_to_win(num) == 10 else 'FAIL')

if __name__ == "__main__":
  test()
