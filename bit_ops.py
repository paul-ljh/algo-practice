from math import log

MAX_BIT_INDEX = 63

def get_bit(num, i):
  if i < 0 or i > MAX_BIT_INDEX:
    return None
  mask = 1 << i
  return mask & num != 0

'''
set i-th bit to 1, 0-based
'''
def set_bit(num, i):
  if i < 0 or i > MAX_BIT_INDEX:
    return None
  mask = 1 << i
  return mask | num

'''
Int in python has 64 bits
1 if non-negative, 0 otherwise
'''
def get_sign(n):
  sign_mask = 1 << MAX_BIT_INDEX
  return int(n & sign_mask == 0)

'''compute the 2's complement of val'''
def twos_comp(bin_seq):
  mask = 1 << MAX_BIT_INDEX
  result = 0
  result += bin_seq & (mask - 1)
  if get_sign(bin_seq) == 0:
    result -= mask
  return result
