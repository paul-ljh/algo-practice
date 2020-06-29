import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from bit_ops import get_sign, twos_comp
from sys import maxsize

def add_without_plus(n1, n2):
  if n1 == 0 or n2 == 0:
    return n1 | n2
  
  n1_sign, n2_sign = get_sign(n1), get_sign(n2)
  result = carry_on = 0
  mask = 1

  while mask >> 64 == 0:
    n1_bit, n2_bit = n1 & mask, n2 & mask
    result |= (n1_bit ^ n2_bit ^ (carry_on << 1))

    if carry_on == 0:
      carry_on = n1_bit & n2_bit
    else:
      carry_on = n1_bit | n2_bit
    mask <<= 1
  
  # Integer Overflow
  if n1_sign == n2_sign and get_sign(result) != n1_sign:
      result = maxsize if n1_sign else -maxsize-1
  return twos_comp(result)

def better_add_without_plus(a, b):
  a_sign, b_sign = get_sign(a), get_sign(b)
  while b != 0:
    result, carry = a ^ b, a & b
    a, b = result, carry << 1
  
  # Integer Overflow
  if a_sign == b_sign and get_sign(a) != a_sign:
    a = maxsize if a_sign else -maxsize-1
  return twos_comp(a)
    

def test():
  n1 = 0
  n2 = 0
  answer = 0
  print('PASS' if better_add_without_plus(n1, n2) == add_without_plus(n1, n2) == answer else 'FAIL')
  
  n1 = 0
  n2 = 0b101011
  answer = n2
  print('PASS' if better_add_without_plus(n1, n2) == add_without_plus(n1, n2) == answer else 'FAIL')
  
  n1 = 0b110011
  n2 = 0b101011
  answer = 0b1011110
  print('PASS' if better_add_without_plus(n1, n2) == add_without_plus(n1, n2) == answer else 'FAIL')
  
  n1 = maxsize
  n2 = 0b11
  answer = maxsize
  print('PASS' if better_add_without_plus(n1, n2) == add_without_plus(n1, n2) == answer else 'FAIL')
  
  n1 = -2
  n2 = -4
  answer = -6
  print('PASS' if better_add_without_plus(n1, n2) == add_without_plus(n1, n2) == answer else 'FAIL')
  
  n1 = -maxsize
  n2 = -4
  answer = -maxsize-1
  print('PASS' if better_add_without_plus(n1, n2) == add_without_plus(n1, n2) == answer else 'FAIL')
  
if __name__ == "__main__":
  test()
  